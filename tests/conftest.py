"""Shared fixtures: the real data set and small hand-made frames."""

import matplotlib
import pandas as pd
import pytest

matplotlib.use("Agg")

from movie_regression.application.cleaning import (  # noqa: E402
    prepare,
    remove_unreleased,
)
from movie_regression.infrastructure.data import load_films  # noqa: E402


@pytest.fixture(scope="session")
def raw_films() -> pd.DataFrame:
    return load_films()


@pytest.fixture(scope="session")
def films(raw_films: pd.DataFrame) -> pd.DataFrame:
    return prepare(raw_films)


@pytest.fixture(scope="session")
def clean_films(films: pd.DataFrame) -> pd.DataFrame:
    return remove_unreleased(films)


@pytest.fixture
def small_raw() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "Rank": [1, 2, 3, 4],
            "Release_Date": ["8/2/1915", "5/9/1969", "1/1/1992", "6/1/2018"],
            "Movie_Title": ["A", "B", "C", "D"],
            "USD_Production_Budget": ["$1,000", "$2,000", "$3,000", "$4,000"],
            "USD_Worldwide_Gross": ["$0", "$500", "$9,000", "$0"],
            "USD_Domestic_Gross": ["$0", "$0", "$4,000", "$0"],
        }
    )


@pytest.fixture
def small_films(small_raw: pd.DataFrame) -> pd.DataFrame:
    return prepare(small_raw)
