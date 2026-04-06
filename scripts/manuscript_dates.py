"""
Per-paper manuscript dates (2025-01-01 .. 2026-12-31), reproducible and unique.

Dates used in ~/Desktop/advanced_research_portfolio/ are EXCLUDED so the two
portfolios never share the same calendar day for any manuscript line.
"""
from __future__ import annotations

import json
import random
from datetime import date, timedelta
from pathlib import Path

# From advanced_research_portfolio/results/paper_manuscript_dates.json (do not reuse)
_FORBIDDEN: frozenset[date] = frozenset(
    {
        date(2026, 1, 25),
        date(2025, 12, 28),
        date(2026, 10, 17),
        date(2025, 2, 27),
        date(2026, 1, 30),
        date(2026, 3, 11),
        date(2026, 1, 7),
        date(2025, 5, 5),
        date(2025, 2, 7),
        date(2026, 7, 7),
    }
)

_START = date(2025, 1, 1)
_END = date(2026, 12, 31)
_SHUFFLE_SEED = 77_777_777


def _eligible_days() -> list[date]:
    out: list[date] = []
    d = _START
    while d <= _END:
        if d not in _FORBIDDEN:
            out.append(d)
        d += timedelta(days=1)
    return out


def manuscript_date_for_paper(paper_id: int, n_papers: int = 30) -> str:
    """
    Return ISO date for paper_id in 1..n_papers.
    Uses a fixed shuffle so the same id always maps to the same date.
    """
    if paper_id < 1 or paper_id > n_papers:
        raise ValueError(f"paper_id must be 1..{n_papers}, got {paper_id}")
    eligible = _eligible_days()
    if len(eligible) < n_papers:
        raise RuntimeError("Not enough eligible days (check date range / forbidden set)")
    rng = random.Random(_SHUFFLE_SEED)
    order = eligible.copy()
    rng.shuffle(order)
    return order[paper_id - 1].isoformat()


def write_dates_manifest(results_dir: Path, n_papers: int = 30) -> Path:
    results_dir.mkdir(parents=True, exist_ok=True)
    mapping = {f"paper_{i}": manuscript_date_for_paper(i, n_papers) for i in range(1, n_papers + 1)}
    path = results_dir / "paper_manuscript_dates.json"
    path.write_text(json.dumps(mapping, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    p = write_dates_manifest(root / "results")
    print(p.read_text(encoding="utf-8"))
