"""Infrastructure: read the film CSV file into a DataFrame."""

from pathlib import Path

import pandas as pd

DATA_FILE: Path = (
    Path(__file__).resolve().parents[3] / "data" / "cost_revenue_dirty.csv"
)


def load_films(path: Path | str | None = None) -> pd.DataFrame:
    """Load cost_revenue_dirty.csv as it is: money columns are still text."""
    return pd.read_csv(DATA_FILE if path is None else Path(path))
