"""Lecture steps 2 and 3: explore and clean the data."""

from dataclasses import dataclass

import pandas as pd

from movie_regression.domain.rules import (
    CHARS_TO_REMOVE,
    DATA_COLLECTION_DATE,
    MONEY_COLUMNS,
    RELEASE_DATE,
)


@dataclass(frozen=True)
class Structure:
    """The answers to the first challenge: how the data is structured."""

    rows: int
    columns: int
    has_nan: bool
    duplicate_rows: int
    dtypes: dict[str, str]


def describe_structure(data: pd.DataFrame) -> Structure:
    """Rows, columns, NaN values, duplicate rows and column types."""
    return Structure(
        rows=data.shape[0],
        columns=data.shape[1],
        has_nan=bool(data.isna().values.any()),
        duplicate_rows=len(data[data.duplicated()]),
        dtypes={name: str(kind) for name, kind in data.dtypes.items()},
    )


def convert_money_to_numbers(data: pd.DataFrame) -> pd.DataFrame:
    """Remove `$` and `,` from the money columns and make them integers.

    Returns a copy; the nested loop is the one of the lecture.
    """
    cleaned = data.copy()
    for column in MONEY_COLUMNS:
        for character in CHARS_TO_REMOVE:
            cleaned[column] = (
                cleaned[column].astype(str).str.replace(character, "", regex=False)
            )
        cleaned[column] = pd.to_numeric(cleaned[column])
    return cleaned


def convert_release_date(data: pd.DataFrame) -> pd.DataFrame:
    """Turn `Release_Date` into a pandas datetime column (returns a copy)."""
    converted = data.copy()
    converted[RELEASE_DATE] = pd.to_datetime(converted[RELEASE_DATE])
    return converted


def prepare(raw: pd.DataFrame) -> pd.DataFrame:
    """Challenges 2 and 3 of the lecture: numeric money and a datetime."""
    return convert_release_date(convert_money_to_numbers(raw))


def unreleased_films(data: pd.DataFrame) -> pd.DataFrame:
    """Films released after the data was collected (1 May 2018)."""
    return data[data[RELEASE_DATE] > DATA_COLLECTION_DATE]


def remove_unreleased(data: pd.DataFrame) -> pd.DataFrame:
    """`data_clean` of the lecture: the data without the unreleased films."""
    return data.drop(unreleased_films(data).index)
