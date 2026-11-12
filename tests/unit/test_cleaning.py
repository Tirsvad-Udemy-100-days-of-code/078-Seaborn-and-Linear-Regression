import pandas as pd

from movie_regression.application import cleaning


def test_describe_structure_counts_rows_columns_and_duplicates(
    small_raw: pd.DataFrame,
) -> None:
    doubled = pd.concat([small_raw, small_raw.iloc[[0]]])

    structure = cleaning.describe_structure(doubled)

    assert (structure.rows, structure.columns) == (5, 6)
    assert structure.duplicate_rows == 1
    assert structure.has_nan is False


def test_describe_structure_detects_nan(small_raw: pd.DataFrame) -> None:
    small_raw.loc[0, "Movie_Title"] = None

    assert cleaning.describe_structure(small_raw).has_nan is True


def test_convert_money_to_numbers_strips_symbols(small_raw: pd.DataFrame) -> None:
    converted = cleaning.convert_money_to_numbers(small_raw)

    assert converted["USD_Production_Budget"].tolist() == [1000, 2000, 3000, 4000]
    assert converted["USD_Worldwide_Gross"].tolist() == [0, 500, 9000, 0]
    assert small_raw["USD_Production_Budget"][0] == "$1,000"


def test_convert_release_date_makes_datetimes(small_raw: pd.DataFrame) -> None:
    converted = cleaning.convert_release_date(small_raw)

    assert converted["Release_Date"][0] == pd.Timestamp(1915, 8, 2)


def test_unreleased_films_are_after_collection_date(
    small_films: pd.DataFrame,
) -> None:
    assert cleaning.unreleased_films(small_films)["Movie_Title"].tolist() == ["D"]


def test_remove_unreleased_keeps_the_others(small_films: pd.DataFrame) -> None:
    kept = cleaning.remove_unreleased(small_films)

    assert kept["Movie_Title"].tolist() == ["A", "B", "C"]


def test_remove_unreleased_changes_nothing_when_all_released(
    small_films: pd.DataFrame,
) -> None:
    released = cleaning.remove_unreleased(small_films)

    assert len(cleaning.remove_unreleased(released)) == len(released)
