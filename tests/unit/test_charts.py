from pathlib import Path

import pandas as pd
from matplotlib.figure import Figure

from movie_regression.presentation import charts


def test_scatter_chart_returns_a_figure(small_films: pd.DataFrame) -> None:
    fig = charts.scatter_chart(small_films)

    assert isinstance(fig, Figure)
    assert fig.axes[0].get_xlabel() == "USD_Production_Budget"


def test_bubble_chart_has_lecture_labels_and_limits(small_films: pd.DataFrame) -> None:
    ax = charts.bubble_chart(small_films).axes[0]

    assert ax.get_ylabel() == "Revenue in $ billions"
    assert ax.get_xlabel() == "Budget in $100 millions"
    assert ax.get_ylim() == (0, 3e9)
    assert ax.get_xlim() == (0, 4.5e8)


def test_bubble_chart_by_date_has_lecture_labels(small_films: pd.DataFrame) -> None:
    ax = charts.bubble_chart_by_date(small_films).axes[0]

    assert ax.get_xlabel() == "Year"
    assert ax.get_ylabel() == "Budget in $ millions"


def test_decade_chart_has_one_bar_per_decade(small_films: pd.DataFrame) -> None:
    ax = charts.decade_chart(small_films).axes[0]

    assert len(ax.patches) == 4
    assert ax.get_xlabel() == "Decade"


def test_regression_chart_default_has_title(small_films: pd.DataFrame) -> None:
    fig = charts.regression_chart(small_films, title="Old films")

    assert fig.axes[0].get_title() == "Old films"


def test_regression_chart_styled_limits_axes(small_films: pd.DataFrame) -> None:
    fig = charts.regression_chart(
        small_films,
        dot_colour=charts.NEW_FILMS_DOT_COLOUR,
        line_colour=charts.NEW_FILMS_LINE_COLOUR,
        title="New films",
    )
    ax = fig.axes[0]

    assert ax.get_xlim()[0] == 0
    assert ax.get_ylim()[0] == 0
    assert ax.get_ylabel() == "Revenue in $ billions"


def test_table_figure_draws_a_table(small_films: pd.DataFrame) -> None:
    fig = charts.table_figure(small_films.head(2), "Films")

    assert len(fig.axes[0].tables) == 1
    assert fig.axes[0].get_title() == "Films"


def test_save_figure_writes_a_png(small_films: pd.DataFrame, tmp_path: Path) -> None:
    target = tmp_path / "scatter.png"

    charts.save_figure(charts.scatter_chart(small_films), target)

    assert target.stat().st_size > 0
