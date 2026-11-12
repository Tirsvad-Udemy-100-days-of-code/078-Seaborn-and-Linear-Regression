import pandas as pd

from movie_regression.application import analysis


def titles(frame: pd.DataFrame) -> list[str]:
    return frame["Movie_Title"].tolist()


def test_summary_statistics_has_mean_row(small_films: pd.DataFrame) -> None:
    stats = analysis.summary_statistics(small_films)

    assert stats.loc["mean", "USD_Production_Budget"] == 2500


def test_lowest_and_highest_budget_films(small_films: pd.DataFrame) -> None:
    assert titles(analysis.lowest_budget_films(small_films)) == ["A"]
    assert titles(analysis.highest_budget_films(small_films, 2)) == ["D", "C"]


def test_zero_domestic_films_sorted_dearest_first(small_films: pd.DataFrame) -> None:
    assert titles(analysis.zero_domestic_films(small_films)) == ["D", "B", "A"]


def test_zero_worldwide_films_sorted_dearest_first(small_films: pd.DataFrame) -> None:
    assert titles(analysis.zero_worldwide_films(small_films)) == ["D", "A"]


def test_international_releases_loc_and_query_agree(small_films: pd.DataFrame) -> None:
    by_loc = analysis.international_releases(small_films)
    by_query = analysis.international_releases_query(small_films)

    assert titles(by_loc) == ["B"]
    assert by_loc.equals(by_query)


def test_international_releases_empty_when_none_match(
    small_films: pd.DataFrame,
) -> None:
    assert analysis.international_releases(small_films.iloc[[2]]).empty


def test_share_losing_money_is_a_percentage(small_films: pd.DataFrame) -> None:
    assert analysis.share_losing_money(small_films) == 75.0


def test_add_decade_returns_a_copy_with_decades(small_films: pd.DataFrame) -> None:
    with_decade = analysis.add_decade(small_films)

    assert with_decade["Decade"].tolist() == [1910, 1960, 1990, 2010]
    assert "Decade" not in small_films.columns


def test_split_old_and_new_at_1970(small_films: pd.DataFrame) -> None:
    old, new = analysis.split_old_and_new(small_films)

    assert titles(old) == ["A", "B"]
    assert titles(new) == ["C", "D"]


def test_films_per_decade_counts_and_sorts(small_films: pd.DataFrame) -> None:
    counts = analysis.films_per_decade(small_films)

    assert counts.to_dict() == {1910: 1, 1960: 1, 1990: 1, 2010: 1}
