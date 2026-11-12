"""Assertions on the 5,391 films of cost_revenue_dirty.csv."""

import pandas as pd
import pytest

from movie_regression.application import analysis, cleaning
from movie_regression.application.regression import fit_budget_to_revenue


def test_structure_is_5391_rows_by_6_columns(raw_films: pd.DataFrame) -> None:
    structure = cleaning.describe_structure(raw_films)

    assert (structure.rows, structure.columns) == (5391, 6)
    assert structure.has_nan is False
    assert structure.duplicate_rows == 0


def test_summary_statistics_match_the_lecture(films: pd.DataFrame) -> None:
    stats = analysis.summary_statistics(films)

    assert stats.loc["mean", "USD_Production_Budget"] == pytest.approx(31113737.58)
    assert stats.loc["mean", "USD_Worldwide_Gross"] == pytest.approx(88855421.96)
    assert stats.loc["max", "USD_Production_Budget"] == 425_000_000
    assert stats.loc["max", "USD_Worldwide_Gross"] == 2_783_918_982


def test_lowest_budget_film_is_my_date_with_drew(films: pd.DataFrame) -> None:
    film = analysis.lowest_budget_films(films).iloc[0]

    assert film["Movie_Title"] == "My Date With Drew"
    assert film["USD_Production_Budget"] == 1100
    assert film["USD_Worldwide_Gross"] == 181_041


def test_zero_gross_counts(films: pd.DataFrame) -> None:
    assert len(analysis.zero_domestic_films(films)) == 512
    assert len(analysis.zero_worldwide_films(films)) == 357


def test_international_releases_loc_equals_query(films: pd.DataFrame) -> None:
    by_loc = analysis.international_releases(films)
    by_query = analysis.international_releases_query(films)

    assert len(by_loc) == len(by_query) == 155


def test_seven_films_are_unreleased(
    films: pd.DataFrame, clean_films: pd.DataFrame
) -> None:
    assert len(cleaning.unreleased_films(films)) == 7
    assert len(clean_films) == 5384


def test_share_losing_money_after_removing_unreleased(
    clean_films: pd.DataFrame,
) -> None:
    assert analysis.share_losing_money(clean_films) == pytest.approx(37.277, abs=1e-3)


def test_old_and_new_film_counts(
    films: pd.DataFrame, clean_films: pd.DataFrame
) -> None:
    old, new = analysis.split_old_and_new(films)
    clean_old, clean_new = analysis.split_old_and_new(clean_films)

    assert (len(old), len(new)) == (153, 5238)
    assert (len(clean_old), len(clean_new)) == (153, 5231)


def test_old_films_regression_has_a_low_r_squared(clean_films: pd.DataFrame) -> None:
    old, _ = analysis.split_old_and_new(clean_films)

    result = fit_budget_to_revenue(old)

    assert result.intercept == pytest.approx(22_821_538.64, rel=1e-6)
    assert result.slope == pytest.approx(1.64771, rel=1e-4)
    assert result.r_squared == pytest.approx(0.02937, rel=1e-3)
    assert result.predict(150_000_000) == pytest.approx(269_978_510, rel=1e-6)


def test_new_films_regression_matches_the_lecture(clean_films: pd.DataFrame) -> None:
    _, new = analysis.split_old_and_new(clean_films)

    result = fit_budget_to_revenue(new)

    assert result.intercept == pytest.approx(-8_650_768.01, rel=1e-6)
    assert result.slope == pytest.approx(3.12260, rel=1e-4)
    assert result.r_squared == pytest.approx(0.55770, rel=1e-4)
    assert result.predict(150_000_000) == pytest.approx(459_738_620, rel=1e-6)
