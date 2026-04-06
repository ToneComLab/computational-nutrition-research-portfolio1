"""Download public data into data/raw/."""
from __future__ import annotations

import json
import time
from pathlib import Path
from urllib.parse import urlencode

import pandas as pd
import requests

from config import (
    DATA_RAW,
    LOGS,
    NHANES_2011,
    NHANES_2017,
    NHANES_BASE,
    OPEN_NUTRITION,
    PUBMED_EUTILS,
    USDA_FDC_API,
    USDA_API_KEY,
    WHO_GHO_API,
    WB_API,
)


def _log(msg: str) -> None:
    p = LOGS / "data_collection.log"
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def _download(url: str, dest: Path, timeout: int = 120) -> bool:
    try:
        r = requests.get(url, timeout=timeout, headers={"User-Agent": "elite-research-portfolio/1.0"})
        r.raise_for_status()
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(r.content)
        return True
    except Exception as e:
        _log(f"FAIL {url} -> {dest}: {e}")
        return False


def download_nhanes_cycle(name: str, urls: dict[str, str]) -> dict[str, Path]:
    out: dict[str, Path] = {}
    for key, url in urls.items():
        dest = DATA_RAW / "nhanes" / name / f"{key}.xpt"
        _download(url, dest)
        out[key] = dest
    return out


def read_nhanes_xpt(path: Path) -> pd.DataFrame:
    if not path.exists() or path.stat().st_size < 100:
        raise FileNotFoundError(path)
    return pd.read_sas(str(path), format="xport", encoding="utf-8")


def fetch_usda_fdc_sample(max_items: int = 40) -> pd.DataFrame:
    url = f"{USDA_FDC_API}foods/list?api_key={USDA_API_KEY}"
    try:
        r = requests.post(
            url,
            json={"pageSize": max_items, "pageNumber": 1, "dataType": ["Foundation", "SR Legacy"]},
            timeout=60,
        )
        r.raise_for_status()
        foods = r.json().get("foods", [])
        rows = []
        for f in foods:
            row = {"fdc_id": f.get("fdcId"), "description": f.get("description", "")}
            for n in f.get("foodNutrients", []) or []:
                nn = n.get("nutrient", {}) or {}
                nm = (nn.get("name") or "").lower().replace(" ", "_")
                if nm:
                    row[nm] = n.get("amount")
            rows.append(row)
        df = pd.DataFrame(rows)
        df.to_csv(DATA_RAW / "usda_fdc_sample.csv", index=False)
        return df
    except Exception as e:
        _log(f"USDA: {e}")
        return pd.DataFrame()


def fetch_pubmed_counts(queries: list[str]) -> pd.DataFrame:
    rows = []
    for q in queries:
        params = urlencode({"db": "pubmed", "term": q, "retmode": "json", "retmax": 0})
        try:
            r = requests.get(f"{PUBMED_EUTILS}esearch.fcgi?{params}", timeout=30)
            r.raise_for_status()
            c = int(r.json()["esearchresult"]["count"])
            rows.append({"query": q, "count": c})
            time.sleep(0.34)
        except Exception as e:
            _log(f"PubMed {q}: {e}")
            rows.append({"query": q, "count": 0})
    df = pd.DataFrame(rows)
    df.to_csv(DATA_RAW / "pubmed_counts.csv", index=False)
    return df


def fetch_who(indicator: str) -> pd.DataFrame:
    try:
        r = requests.get(f"{WHO_GHO_API}{indicator}", timeout=90)
        r.raise_for_status()
        df = pd.json_normalize(r.json().get("value", []))
        df.to_csv(DATA_RAW / f"who_{indicator}.csv", index=False)
        return df
    except Exception as e:
        _log(f"WHO {indicator}: {e}")
        return pd.DataFrame()


def fetch_worldbank_indicator(indicator: str, per_page: int = 5000) -> pd.DataFrame:
    """World Bank API — e.g. SP.POP.TOTL, SN.ITK.DEFC.ZS"""
    url = f"{WB_API}country/all/indicator/{indicator}?format=json&per_page={per_page}"
    try:
        r = requests.get(url, timeout=120)
        r.raise_for_status()
        js = r.json()
        if len(js) < 2:
            return pd.DataFrame()
        df = pd.DataFrame(js[1])
        df.to_csv(DATA_RAW / f"wb_{indicator}.csv", index=False)
        return df
    except Exception as e:
        _log(f"WorldBank {indicator}: {e}")
        return pd.DataFrame()


def download_open_nutrition() -> None:
    dest = DATA_RAW / "open_nutrition.csv"
    if not _download(OPEN_NUTRITION, dest):
        pd.DataFrame({"note": ["placeholder"]}).to_csv(dest, index=False)


def collect_all() -> dict:
    manifest: dict = {"nhanes_portal": NHANES_BASE, "cycles": {}}
    manifest["cycles"]["2017_2018"] = {k: str(v) for k, v in download_nhanes_cycle("2017_2018", NHANES_2017).items()}
    manifest["cycles"]["2011_2012"] = {k: str(v) for k, v in download_nhanes_cycle("2011_2012", NHANES_2011).items()}
    fetch_usda_fdc_sample(40)
    manifest["usda"] = str(DATA_RAW / "usda_fdc_sample.csv")
    fetch_pubmed_counts(
        ["functional food", "bioactive compound", "dietary guideline", "ultra-processed", "NHANES diet"]
    )
    manifest["pubmed"] = str(DATA_RAW / "pubmed_counts.csv")
    for ind in ("NUTRITION_HA_1", "NUTRITION_HA_2"):
        fetch_who(ind)
    fetch_worldbank_indicator("SP.POP.TOTL")
    fetch_worldbank_indicator("SH.STA.OV25.ZS")
    download_open_nutrition()
    manifest["open_nutrition"] = str(DATA_RAW / "open_nutrition.csv")
    manifest["urls"] = {
        "fao": "https://www.fao.org/faostat/",
        "worldbank": "https://data.worldbank.org/",
    }
    (DATA_RAW / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    return manifest


if __name__ == "__main__":
    collect_all()
