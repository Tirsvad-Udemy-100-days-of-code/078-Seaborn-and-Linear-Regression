"""Smoke test: the package imports and the dataset is in place."""

from pathlib import Path

import movie_regression

DATA = Path(__file__).resolve().parents[2] / "data" / "cost_revenue_dirty.csv"


def test_package_has_a_version() -> None:
    assert movie_regression.__version__ == "0.1.0"


def test_dataset_is_present() -> None:
    assert DATA.is_file()
