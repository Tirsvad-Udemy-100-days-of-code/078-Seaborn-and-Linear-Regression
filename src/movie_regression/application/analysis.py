"""Lecture steps 3 to 6: statistics, filters and decades."""

import pandas as pd

from movie_regression.domain.rules import (
    BUDGET,
    DECADE,
    DOMESTIC,
    OLD_FILMS_BEFORE_YEAR,
    RELEASE_DATE,
    WORLDWIDE,
    to_decade,
)


def summary_statistics(data: pd.DataFrame) -> pd.DataFrame:
    """`.describe()`: mean, minimum, quartiles and maximum of every column."""
    return data.describe()


def lowest_budget_films(data: pd.DataFrame, count: int = 1) -> pd.DataFrame:
    """The films with the smallest production budget."""
    return data.nsmallest(count, BUDGET)


def highest_budget_films(data: pd.DataFrame, count: int = 1) -> pd.DataFrame:
    """The films with the largest production budget."""
    return data.nlargest(count, BUDGET)


def zero_domestic_films(data: pd.DataFrame) -> pd.DataFrame:
    """Films that grossed nothing in the United States, dearest first."""
    return data[data[DOMESTIC] == 0].sort_values(BUDGET, ascending=False)


def zero_worldwide_films(data: pd.DataFrame) -> pd.DataFrame:
    """Films that grossed nothing anywhere, dearest first (the biggest flops)."""
    return data[data[WORLDWIDE] == 0].sort_values(BUDGET, ascending=False)


def international_releases(data: pd.DataFrame) -> pd.DataFrame:
    """Zero domestic gross but some worldwide gross, with `.loc[]` and `&`."""
    return data.loc[(data[DOMESTIC] == 0) & (data[WORLDWIDE] != 0)]


def international_releases_query(data: pd.DataFrame) -> pd.DataFrame:
    """The same filter written as a `.query()` string."""
    return data.query(f"{DOMESTIC} == 0 and {WORLDWIDE} != 0")


def share_losing_money(data: pd.DataFrame) -> float:
    """Percentage of films whose budget exceeds their worldwide gross."""
    return float((data[BUDGET] > data[WORLDWIDE]).mean() * 100)


def add_decade(data: pd.DataFrame) -> pd.DataFrame:
    """Add a `Decade` column using floor division (returns a copy)."""
    with_decade = data.copy()
    release_years = pd.DatetimeIndex(with_decade[RELEASE_DATE]).year
    with_decade[DECADE] = to_decade(release_years)
    return with_decade


def split_old_and_new(data: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Films of decades before 1970 (old) and from 1970 (new)."""
    with_decade = data if DECADE in data.columns else add_decade(data)
    old = with_decade[with_decade[DECADE] < OLD_FILMS_BEFORE_YEAR]
    new = with_decade[with_decade[DECADE] >= OLD_FILMS_BEFORE_YEAR]
    return old, new


def films_per_decade(data: pd.DataFrame) -> pd.Series:
    """How many films were released in each decade."""
    with_decade = data if DECADE in data.columns else add_decade(data)
    return with_decade[DECADE].value_counts().sort_index()
