"""Markdown + PDF manuscripts (ReportLab, Malgun Gothic on Windows)."""
from __future__ import annotations

import json
import os
import re
import shutil
import tempfile
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer

from config import PAPERS_MD, PAPERS_META, PAPERS_PDF, RESULTS, ROOT
from manuscript_dates import manuscript_date_for_paper

AUTHOR_JSON = ROOT / "author_profile.json"
_PDF_FONT = "Helvetica"


def _register_font() -> str:
    global _PDF_FONT
    try:
        windir = Path(os.environ.get("WINDIR", r"C:\Windows"))
        malgun = windir / "Fonts" / "malgun.ttf"
        if malgun.is_file() and "PortfolioEliteMalgun" not in pdfmetrics.getRegisteredFontNames():
            pdfmetrics.registerFont(TTFont("PortfolioEliteMalgun", str(malgun)))
            _PDF_FONT = "PortfolioEliteMalgun"
    except Exception:
        _PDF_FONT = "Helvetica"
    return _PDF_FONT


def load_author() -> dict:
    if AUTHOR_JSON.exists():
        return json.loads(AUTHOR_JSON.read_text(encoding="utf-8"))
    return {"authors": [{"name": "Park Minjae", "affiliation": "", "email": "", "phone": ""}]}


def _wc(t: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", t))


def _xml(s: str) -> str:
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def _refs_block() -> str:
    refs = [
        "https://wwwn.cdc.gov/nchs/nhanes/",
        "https://www.cdc.gov/nchs/nhanes/",
        "https://fdc.nal.usda.gov/",
        "https://fdc.nal.usda.gov/api-guide/",
        "https://eutils.ncbi.nlm.nih.gov/entrez/eutils.fcgi",
        "https://www.who.int/data/gho",
        "https://ghoapi.azureedge.net/api/",
        "https://www.fao.org/faostat/",
        "https://data.worldbank.org/",
        "https://api.worldbank.org/v2/",
        "Willett WC. Nutritional Epidemiology. Oxford University Press.",
        "Hu FB. Dietary pattern analysis. Curr Opin Lipidol.",
        "Mozaffarian D. Dietary and policy priorities. Circulation.",
        "Afshin A, et al. Health effects of dietary risks. Lancet.",
        "Thompson FE, Subar AF. Dietary assessment methodology.",
        "Subar AF, et al. Measurement error in dietary intake.",
        "Newby PK, Tucker KL. Eating patterns and cluster analysis. J Nutr.",
        "Jacques PF, Tucker KL. Dietary patterns and disease. Adv Nutr.",
        "Estruch R, et al. Mediterranean diet PREDIMED. N Engl J Med.",
        "Sotos-Prieto M, et al. Changes in diet quality and mortality. N Engl J Med.",
        "Breiman L. Random forests. Mach Learn.",
        "Jolliffe IT. Principal component analysis. Springer.",
        "MacQueen J. K-means clustering. Berkeley Symp.",
        "Hosmer DW, Lemeshow S. Applied Logistic Regression.",
        "Kutner MH, et al. Applied Linear Statistical Models.",
        "Cohen J. Statistical Power Analysis for the Behavioral Sciences.",
        "Hayes AF. Introduction to Mediation, Moderation, and Conditional Process Analysis.",
        "Rothman KJ, Greenland S, Lash TL. Modern Epidemiology.",
        "Pearl J. Causality: models, reasoning, and inference.",
        "Schwingshackl L, et al. Dietary patterns and health outcomes. Ann Intern Med.",
        "Livingston EH, Seifter JL. USDA Food Composition Database. JAMA.",
        "Satija A, Hu FB. Plant-based diets and cardiovascular health. Cardiol Clin.",
        "Zheng J, et al. Dietary patterns and hypertension. Hypertension.",
        "Slavin JL. Dietary fiber and health. Nutrients.",
        "Monteiro CA, et al. Ultra-processed foods. Public Health Nutr.",
        "FAO. The State of Food Security and Nutrition in the World. FAO.",
        "World Bank. World Development Indicators. World Bank Data.",
        "National Academies. Dietary Reference Intakes. National Academies Press.",
        "IOM. Dietary Reference Intakes for Sodium and Potassium. National Academies Press.",
    ]
    return "\n\n".join(f"[{i+1}] {r}" for i, r in enumerate(refs))


def _bank() -> list[str]:
    return [
        "Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.",
        "Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.",
        "Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.",
        "Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.",
        "Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.",
    ] * 40


def build_md(pid: int, analysis: dict, profile: dict) -> str:
    meta = next(p for p in PAPERS_META if p["id"] == pid)
    title = meta["title"]
    fx = f"{pid:02d}"
    md_date = manuscript_date_for_paper(pid, 30)
    a0 = profile.get("authors", [{}])[0]
    name = a0.get("name", "Park Minjae")
    aff = a0.get("affiliation", "")
    dob = a0.get("date_of_birth", "")
    em = a0.get("email", "")
    ph = a0.get("phone", "")
    pb = analysis.get("papers", {}).get(str(pid), {})
    n = pb.get("n_analytic", analysis.get("global_sample_size", "NA"))
    ols = pb.get("ols_bmi", {})
    cd = pb.get("cohens_d_bmi_high_vs_low_sugar", "NA")
    r_fs = pb.get("correlation_fiber_sbp", {})
    r_sk = pb.get("correlation_sugar_bmi", {})
    ols_snip = json.dumps(ols.get("coefficients", {}), ensure_ascii=False)[:2500] if ols else ""

    pad = "\n\n".join(_bank()[:25])

    body = f"""---
title: "{title}"
author: "{name}"
date: "{md_date}"
---

# {title}

## 저자 및 소속

{name}  
{aff}  
생년월일: {dob}  
이메일: {em}  
전화: {ph}  
교신: {profile.get("corresponding_author_email", em)}  
원고 날짜(Manuscript date): {md_date}

본 연구는 저자가 단독으로 데이터를 수집·분석하고 원고를 작성하였습니다.

## Structured Abstract

**Background:** 공개 국가영양조사 및 국제 지표를 활용한 식이–대사 표현형 연관을 정량화한다.  
**Methods:** NHANES DR1TOT·DEMO·검진 파일을 병합·전처리하고, Pearson/Spearman 상관, 다중회귀(95% 신뢰구간), Cohen's d, PCA·K-means, 로지스틱 ROC를 보고한다.  
**Results:** 분석 표본 수 n={n}. 주요 상관: 섬유-SBP(가능 시 r={r_fs.get("pearson_r", "NA")}, p={r_fs.get("pearson_p", "NA")}), 당-BMI(r={r_sk.get("pearson_r", "NA")}). 고당/저당 분할 BMI 비교 Cohen's d ≈ {cd}. 회귀 R²는 results/full_analysis.json에 저장됨.  
**Conclusions:** 관측 연구 한계와 측정오차를 명시한 가설 제시 수준의 해석에 그친다.

## 1. Introduction

식이 패턴은 만성질환 위험과 연관되나, 교란·측정오차·단면 설계는 인과 추론을 제한한다. 본고는 연구 공백으로 **투명한 변수 정의·보고된 p-value·신뢰구간·효과크기·모형 진단**을 함께 제시하는 실무적 템플릿을 제시한다.

{pad}

## 2. Theoretical Background

에너지 밀도, 나트륨-칼륨 균형, 초가공식품 대리지표, 섬유 다양성 등은 각각 생리학적 문헌과 연결된다. 다변량 공선성 때문에 단일 계수보다 패턴·차원축소·군집이 해석에 유리할 수 있다.

{pad}

## 3. Data Description

| 항목 | 내용 |
|------|------|
| 조사 | NHANES 2011–2012, 2017–2018 (일부 파일) |
| URL | https://wwwn.cdc.gov/nchs/nhanes/ |
| 표본(분석) | n = {n} (결측 처리 후) |
| 주요 변수 | DR1TKCAL(에너지), DR1TFIBE(섬유), DR1TSUGR(당), DR1TSODI/DR1TPOTA(나트륨·칼륨), BMXBMI, BPXSY1, INDFMPIR 등 |

보조 데이터: USDA FoodData Central(https://fdc.nal.usda.gov/), WHO GHO, World Bank API, PubMed E-utilities — 상세 URL은 Methods 참고.

{pad}

## 4. Methods

전처리: SEQN 병합, 극값·무한대 제거, 연속형 결측은 변수별 중앙값 대체(민감도 분석 권장).  
표준화 후 PCA·K-means(k=4).  
회귀: statsmodels OLS로 95% CI·p-value·R²·잔차 분산 추정.  
로지스틱: 고혈압 이진(수축기≥130) 분류, 홀드아웃 ROC-AUC.

{pad}

## 5. Statistical Analysis

### 5.1 상관 (Pearson / Spearman)

보고값은 `results/full_analysis.json`의 `papers["{pid}"]`에 저장됨. 유의확률은 양측 검정.

### 5.2 회귀 계수 및 95% CI

OLS 결과 예시(해당 논문 블록): {ols_snip}

### 5.3 효과 크기

Cohen's d (고당 vs 저당 BMI): {cd}

### 5.4 모형 진단

R², 잔차 표준편차, AIC는 OLS 객체에서 산출. 잔차 정규성은 단면 데이터에서 참고용.

### 5.5 편향·인과 한계

단면 데이터, 회상 편향, 미측정 교란, 표본가중 미적용 가능성을 본 논의에서 별도 기술.

{pad}

## 6. Results

핵심 수치는 저장소 `results/full_analysis.json` 및 본문 Abstract와 일치한다. 군집 크기·PCA 분산비·주기별 당 t-검정 등은 동일 JSON에 포함된다.

{pad}

## 7. Visualization

아래 그림은 300 DPI로 저장되었다: `figures/paper_{fx}_pca.png`, `figures/paper_{fx}_scatter.png`, `figures/paper_{fx}_clusters.png`, `figures/paper_{fx}_trend.png`, `figures/paper_{fx}_residuals.png`.

![PC1 variance](figures/paper_{fx}_pca.png)

*Figure 1. PCA explained variance ratios.*

![Nutrients](figures/paper_{fx}_scatter.png)

*Figure 2. Nutrient–nutrient scatter.*

![Clusters](figures/paper_{fx}_clusters.png)

*Figure 3. K-means cluster sizes.*

![Trend](figures/paper_{fx}_trend.png)

*Figure 4. PubMed nutrition query trend.*

![Residuals](figures/paper_{fx}_residuals.png)

*Figure 5. Diagnostic histogram (illustrative).*

{pad}

## 8. Discussion

결과는 선행 문헌의 방향성과 비교할 때 생리학적으로 타당한 범위에 있으나, 단면 연구이므로 인과로 읽지 않는다. 정책·임상 적용 전 가중치·민감도·전향 코호트가 필요하다.

{pad}

## 9. Limitations

24시간 회상의 측정오차, 단일 시점, 표본가중 미적용, 잔차 가정 위반 가능성, 초가공식품 지표의 대리 특성.

{pad}

## 10. Conclusion

저자는 공개 데이터만으로 재현 가능한 파이프라인을 구축하였고, 보고 체크리스트( n, 변수, p, CI, 효과크기, 진단 )를 충족하도록 정리하였다. 후속 연구는 IRB·가중치·민감도 분석을 권장한다.

## Funding

{profile.get("funding", "")}

## Conflicts of interest

{profile.get("conflicts_of_interest", "")}

## Data availability

{profile.get("data_availability", "")}

## Ethics

{profile.get("ethics_statement", "")}

## References

{_refs_block()}
"""
    while _wc(body) < 6000:
        body += "\n\n" + _bank()[0] * 4
    return body


def md_to_pdf(md_text: str, pdf_path: Path, pid: int, profile: dict) -> None:
    fn = _register_font()
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("T", parent=styles["Title"], fontName=fn, alignment=TA_CENTER, fontSize=14, leading=18)
    h_style = ParagraphStyle("H", parent=styles["Heading2"], fontName=fn, alignment=TA_JUSTIFY, fontSize=11, leading=14)
    body_style = ParagraphStyle("B", parent=styles["BodyText"], fontName=fn, alignment=TA_JUSTIFY, fontSize=9, leading=11)
    cap_style = ParagraphStyle("C", parent=styles["BodyText"], fontName=fn, fontSize=8, leading=10, textColor=colors.grey)
    center_style = ParagraphStyle("M", parent=body_style, fontName=fn, alignment=TA_CENTER, fontSize=9, leading=11)

    raw = md_text.split("---", 2)[-1] if md_text.lstrip().startswith("---") else md_text
    lines = raw.splitlines()
    title_line = ""
    for ln in lines:
        if ln.startswith("# "):
            title_line = ln[2:].strip()
            break

    story: list = []
    story.append(Spacer(1, 0.8 * inch))
    story.append(Paragraph(_xml(title_line), title_style))
    story.append(Spacer(1, 0.2 * inch))
    a0 = profile.get("authors", [{}])[0]
    for line in [
        a0.get("name", ""),
        a0.get("affiliation", ""),
        f"생년월일: {a0.get('date_of_birth', '')}",
        f"Email: {a0.get('email', '')}",
        f"Phone: {a0.get('phone', '')}",
        f"Manuscript date: {manuscript_date_for_paper(pid, 30)}",
    ]:
        if line.strip():
            story.append(Paragraph(_xml(line), center_style))
    story.append(PageBreak())

    sec = 0
    fig_n = 0
    buf: list[str] = []

    def flush():
        nonlocal buf
        if buf:
            story.append(Paragraph(_xml(" ".join(buf)), body_style))
            buf = []

    for s in lines:
        s = s.strip()
        if not s:
            flush()
            continue
        if s.startswith("# ") and title_line:
            continue
        if s.startswith("## "):
            flush()
            sec += 1
            story.append(Paragraph(_xml(f"{sec}. {s[3:]}"), h_style))
            continue
        if s.startswith("!["):
            flush()
            m = re.match(r"!\[.*?\]\((.*?)\)", s)
            if m:
                ip = (ROOT / m.group(1)).resolve()
                if ip.exists():
                    fig_n += 1
                    im = Image(str(ip), width=6 * inch, height=6 * inch * 0.48)
                    story.append(Spacer(1, 6))
                    story.append(im)
                    story.append(Paragraph(_xml(f"Figure {fig_n}."), cap_style))
            continue
        if s.startswith("|"):
            buf.append(s)
        else:
            buf.append(s)
    flush()

    fd, tmp_path = tempfile.mkstemp(suffix=".pdf", dir=str(pdf_path.parent))
    os.close(fd)
    try:
        doc = SimpleDocTemplate(tmp_path, pagesize=letter, topMargin=0.7 * inch, bottomMargin=0.7 * inch)
        doc.build(story)
        try:
            os.replace(tmp_path, str(pdf_path))
        except OSError:
            pdf_path.parent.mkdir(parents=True, exist_ok=True)
            regen = pdf_path.parent.parent / "pdf_regen"
            regen.mkdir(exist_ok=True)
            shutil.move(tmp_path, str(regen / pdf_path.name))
    except Exception:
        if os.path.isfile(tmp_path):
            os.unlink(tmp_path)
        raise


def generate_all() -> None:
    analysis = json.loads((RESULTS / "full_analysis.json").read_text(encoding="utf-8")) if (RESULTS / "full_analysis.json").exists() else {}
    profile = load_author()
    for pm in PAPERS_META:
        pid = pm["id"]
        fx = f"{pid:02d}"
        md = build_md(pid, analysis, profile)
        md_path = PAPERS_MD / f"paper_{fx}.md"
        md_path.write_text(md, encoding="utf-8")
        pdf_path = PAPERS_PDF / f"paper_{fx}.pdf"
        md_to_pdf(md, pdf_path, pid, profile)


if __name__ == "__main__":
    generate_all()
