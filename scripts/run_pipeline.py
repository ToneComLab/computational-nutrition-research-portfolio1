"""Elite portfolio: collect → preprocess → analyze → dates manifest → figures → papers."""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from analysis import run_analysis  # noqa: E402
from config import RESULTS  # noqa: E402
from data_collection import collect_all  # noqa: E402
from manuscript_dates import write_dates_manifest  # noqa: E402
from paper_generator import generate_all  # noqa: E402
from preprocessing import preprocess  # noqa: E402
from visualization import make_figures  # noqa: E402


def main() -> None:
    collect_all()
    preprocess()
    run_analysis()
    write_dates_manifest(RESULTS, 30)
    make_figures()
    generate_all()


if __name__ == "__main__":
    main()
