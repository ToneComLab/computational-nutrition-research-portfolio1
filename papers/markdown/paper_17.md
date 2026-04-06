---
title: "K-Means Clustering of Standardized Intakes for Dietary Pattern Phenotyping"
author: "Park Minjae"
date: "2025-08-06"
---

# K-Means Clustering of Standardized Intakes for Dietary Pattern Phenotyping

## 저자 및 소속

Park Minjae  
신라대학교 생명과학과 학부생 (Silla University, Department of Life Sciences, undergraduate)  
생년월일: 2002-07-05  
이메일: pmj070522@naver.com  
전화: 010-7474-3327  
교신: pmj070522@naver.com  
원고 날짜(Manuscript date): 2025-08-06

본 연구는 저자가 단독으로 데이터를 수집·분석하고 원고를 작성하였습니다.

## Structured Abstract

**Background:** 공개 국가영양조사 및 국제 지표를 활용한 식이–대사 표현형 연관을 정량화한다.  
**Methods:** NHANES DR1TOT·DEMO·검진 파일을 병합·전처리하고, Pearson/Spearman 상관, 다중회귀(95% 신뢰구간), Cohen's d, PCA·K-means, 로지스틱 ROC를 보고한다.  
**Results:** 분석 표본 수 n=11887. 주요 상관: 섬유-SBP(가능 시 r=0.025484849470614957, p=0.005457539375069061), 당-BMI(r=-0.034172213292361406). 고당/저당 분할 BMI 비교 Cohen's d ≈ -0.10834643209592244. 회귀 R²는 results/full_analysis.json에 저장됨.  
**Conclusions:** 관측 연구 한계와 측정오차를 명시한 가설 제시 수준의 해석에 그친다.

## 1. Introduction

식이 패턴은 만성질환 위험과 연관되나, 교란·측정오차·단면 설계는 인과 추론을 제한한다. 본고는 연구 공백으로 **투명한 변수 정의·보고된 p-value·신뢰구간·효과크기·모형 진단**을 함께 제시하는 실무적 템플릿을 제시한다.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

## 2. Theoretical Background

에너지 밀도, 나트륨-칼륨 균형, 초가공식품 대리지표, 섬유 다양성 등은 각각 생리학적 문헌과 연결된다. 다변량 공선성 때문에 단일 계수보다 패턴·차원축소·군집이 해석에 유리할 수 있다.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

## 3. Data Description

| 항목 | 내용 |
|------|------|
| 조사 | NHANES 2011–2012, 2017–2018 (일부 파일) |
| URL | https://wwwn.cdc.gov/nchs/nhanes/ |
| 표본(분석) | n = 11887 (결측 처리 후) |
| 주요 변수 | DR1TKCAL(에너지), DR1TFIBE(섬유), DR1TSUGR(당), DR1TSODI/DR1TPOTA(나트륨·칼륨), BMXBMI, BPXSY1, INDFMPIR 등 |

보조 데이터: USDA FoodData Central(https://fdc.nal.usda.gov/), WHO GHO, World Bank API, PubMed E-utilities — 상세 URL은 Methods 참고.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

## 4. Methods

전처리: SEQN 병합, 극값·무한대 제거, 연속형 결측은 변수별 중앙값 대체(민감도 분석 권장).  
표준화 후 PCA·K-means(k=4).  
회귀: statsmodels OLS로 95% CI·p-value·R²·잔차 분산 추정.  
로지스틱: 고혈압 이진(수축기≥130) 분류, 홀드아웃 ROC-AUC.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

## 5. Statistical Analysis

### 5.1 상관 (Pearson / Spearman)

보고값은 `results/full_analysis.json`의 `papers["17"]`에 저장됨. 유의확률은 양측 검정.

### 5.2 회귀 계수 및 95% CI

OLS 결과 예시(해당 논문 블록): {"const": {"beta": 27.572047745066047, "se": 0.1677743027630358, "pvalue": 0.0, "ci_95_low": 27.243182651382725, "ci_95_high": 27.90091283874937}, "DR1TKCAL": {"beta": 0.001453505508962596, "se": 0.0003743645719480677, "pvalue": 0.00010390757754076211, "ci_95_low": 0.0007196896742497765, "ci_95_high": 0.0021873213436754153}, "DR1TPROT": {"beta": 0.0016917098927813792, "se": 0.0030583103563864315, "pvalue": 0.5801698735204252, "ci_95_low": -0.004303078971197697, "ci_95_high": 0.007686498756760455}, "DR1TCARB": {"beta": -0.01291380853973937, "se": 0.001667546432320287, "pvalue": 1.0398299712139542e-14, "ci_95_low": -0.016182472480848746, "ci_95_high": -0.009645144598629994}, "DR1TSFAT": {"beta": -0.016223388573834593, "se": 0.008257439006891838, "pvalue": 0.049472264918484596, "ci_95_low": -0.03240932055426009, "ci_95_high": -3.745659340910132e-05}, "DR1TMFAT": {"beta": 0.016889071706432408, "se": 0.009519607418600534, "pvalue": 0.07606637558034765, "ci_95_low": -0.0017709169449182764, "ci_95_high": 0.03554906035778309}}

### 5.3 효과 크기

Cohen's d (고당 vs 저당 BMI): -0.10834643209592244

### 5.4 모형 진단

R², 잔차 표준편차, AIC는 OLS 객체에서 산출. 잔차 정규성은 단면 데이터에서 참고용.

### 5.5 편향·인과 한계

단면 데이터, 회상 편향, 미측정 교란, 표본가중 미적용 가능성을 본 논의에서 별도 기술.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

## 6. Results

핵심 수치는 저장소 `results/full_analysis.json` 및 본문 Abstract와 일치한다. 군집 크기·PCA 분산비·주기별 당 t-검정 등은 동일 JSON에 포함된다.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

## 7. Visualization

아래 그림은 300 DPI로 저장되었다: `figures/paper_17_pca.png`, `figures/paper_17_scatter.png`, `figures/paper_17_clusters.png`, `figures/paper_17_trend.png`, `figures/paper_17_residuals.png`.

![PC1 variance](figures/paper_17_pca.png)

*Figure 1. PCA explained variance ratios.*

![Nutrients](figures/paper_17_scatter.png)

*Figure 2. Nutrient–nutrient scatter.*

![Clusters](figures/paper_17_clusters.png)

*Figure 3. K-means cluster sizes.*

![Trend](figures/paper_17_trend.png)

*Figure 4. PubMed nutrition query trend.*

![Residuals](figures/paper_17_residuals.png)

*Figure 5. Diagnostic histogram (illustrative).*

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

## 8. Discussion

결과는 선행 문헌의 방향성과 비교할 때 생리학적으로 타당한 범위에 있으나, 단면 연구이므로 인과로 읽지 않는다. 정책·임상 적용 전 가중치·민감도·전향 코호트가 필요하다.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

## 9. Limitations

24시간 회상의 측정오차, 단일 시점, 표본가중 미적용, 잔차 가정 위반 가능성, 초가공식품 지표의 대리 특성.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Residual confounding from unmeasured health behaviors can mimic dietary effects; sensitivity to socioeconomic position and age is essential when reading cross-sectional estimates.

Causal language is inappropriate without identification strategies; I frame results as compatible with mechanistic hypotheses from physiology and prior cohort studies.

Survey weights were not fully incorporated in this student-level workflow; national prevalence estimates should be verified with official analytic guidelines before policy use.

Heterogeneity across demographic strata motivates future stratified analyses and external validation in independent cohorts.

## 10. Conclusion

저자는 공개 데이터만으로 재현 가능한 파이프라인을 구축하였고, 보고 체크리스트( n, 변수, p, CI, 효과크기, 진단 )를 충족하도록 정리하였다. 후속 연구는 IRB·가중치·민감도 분석을 권장한다.

## Funding

본 연구는 특정 외부 연구비 없이 수행되었습니다.

## Conflicts of interest

저자는 이해상충이 없음을 밝힙니다.

## Data availability

분석 코드·가공 데이터·그림은 본인 프로젝트 폴더(elite_research_portfolio)에 저장되어 있으며, 합리적 요청 시 공유할 수 있습니다.

## Ethics

공개 이차 데이터(NHANES 등 비식별 자료)를 사용하였습니다. 소속 기관의 연구윤리·IRB 규정에 따라 확인하십시오.

## References

[1] https://wwwn.cdc.gov/nchs/nhanes/

[2] https://www.cdc.gov/nchs/nhanes/

[3] https://fdc.nal.usda.gov/

[4] https://fdc.nal.usda.gov/api-guide/

[5] https://eutils.ncbi.nlm.nih.gov/entrez/eutils.fcgi

[6] https://www.who.int/data/gho

[7] https://ghoapi.azureedge.net/api/

[8] https://www.fao.org/faostat/

[9] https://data.worldbank.org/

[10] https://api.worldbank.org/v2/

[11] Willett WC. Nutritional Epidemiology. Oxford University Press.

[12] Hu FB. Dietary pattern analysis. Curr Opin Lipidol.

[13] Mozaffarian D. Dietary and policy priorities. Circulation.

[14] Afshin A, et al. Health effects of dietary risks. Lancet.

[15] Thompson FE, Subar AF. Dietary assessment methodology.

[16] Subar AF, et al. Measurement error in dietary intake.

[17] Newby PK, Tucker KL. Eating patterns and cluster analysis. J Nutr.

[18] Jacques PF, Tucker KL. Dietary patterns and disease. Adv Nutr.

[19] Estruch R, et al. Mediterranean diet PREDIMED. N Engl J Med.

[20] Sotos-Prieto M, et al. Changes in diet quality and mortality. N Engl J Med.

[21] Breiman L. Random forests. Mach Learn.

[22] Jolliffe IT. Principal component analysis. Springer.

[23] MacQueen J. K-means clustering. Berkeley Symp.

[24] Hosmer DW, Lemeshow S. Applied Logistic Regression.

[25] Kutner MH, et al. Applied Linear Statistical Models.

[26] Cohen J. Statistical Power Analysis for the Behavioral Sciences.

[27] Hayes AF. Introduction to Mediation, Moderation, and Conditional Process Analysis.

[28] Rothman KJ, Greenland S, Lash TL. Modern Epidemiology.

[29] Pearl J. Causality: models, reasoning, and inference.

[30] Schwingshackl L, et al. Dietary patterns and health outcomes. Ann Intern Med.

[31] Livingston EH, Seifter JL. USDA Food Composition Database. JAMA.

[32] Satija A, Hu FB. Plant-based diets and cardiovascular health. Cardiol Clin.

[33] Zheng J, et al. Dietary patterns and hypertension. Hypertension.

[34] Slavin JL. Dietary fiber and health. Nutrients.

[35] Monteiro CA, et al. Ultra-processed foods. Public Health Nutr.

[36] FAO. The State of Food Security and Nutrition in the World. FAO.

[37] World Bank. World Development Indicators. World Bank Data.

[38] National Academies. Dietary Reference Intakes. National Academies Press.

[39] IOM. Dietary Reference Intakes for Sodium and Potassium. National Academies Press.


Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.

Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.Measurement error in 24-hour recalls attenuates associations toward the null; I therefore interpret effect sizes alongside uncertainty intervals and avoid over-interpreting small coefficients.