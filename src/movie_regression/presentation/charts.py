"""Presentation: the charts of the lecture as matplotlib figures.

Figures are built without pyplot, so no global state is shared between tests.
"""

from pathlib import Path

import pandas as pd
import seaborn as sns
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from movie_regression.application.analysis import films_per_decade
from movie_regression.application.regression import RegressionResult
from movie_regression.domain.rules import BUDGET, RELEASE_DATE, WORLDWIDE

FIGURE_SIZE = (8, 4)
COMPARISON_SIZE = (12, 4.5)
FIGURE_DPI = 200
TABLE_FONT_SIZE = 9
TABLE_ROW_INCHES = 0.4
TABLE_INCHES_PER_CHARACTER = 0.085
MAX_REVENUE = 3e9
MAX_BUDGET = 4.5e8
NEW_FILMS_DOT_COLOUR = "#2f4b7c"
NEW_FILMS_LINE_COLOUR = "#ff7c43"


def save_figure(fig: Figure, path: Path | str) -> None:
    """Write the figure to an image file."""
    fig.savefig(Path(path), bbox_inches="tight")


def _new_figure() -> Figure:
    return Figure(figsize=FIGURE_SIZE, dpi=FIGURE_DPI)


def scatter_chart(data: pd.DataFrame) -> Figure:
    """Scatter plot of production budget against worldwide gross."""
    fig = _new_figure()
    ax = fig.add_subplot()
    sns.scatterplot(data=data, x=BUDGET, y=WORLDWIDE, ax=ax)
    return fig


def bubble_chart(data: pd.DataFrame) -> Figure:
    """Budget against revenue, colour and size showing the worldwide gross."""
    fig = _new_figure()
    ax = fig.add_subplot()
    with sns.axes_style("darkgrid"):
        sns.scatterplot(
            data=data, x=BUDGET, y=WORLDWIDE, hue=WORLDWIDE, size=WORLDWIDE, ax=ax
        )
    ax.set(
        ylim=(0, MAX_REVENUE),
        xlim=(0, MAX_BUDGET),
        ylabel="Revenue in $ billions",
        xlabel="Budget in $100 millions",
    )
    return fig


def bubble_chart_by_date(data: pd.DataFrame) -> Figure:
    """Budget over the release date, colour and size showing the gross."""
    fig = _new_figure()
    ax = fig.add_subplot()
    with sns.axes_style("whitegrid"):
        sns.scatterplot(
            data=data,
            x=RELEASE_DATE,
            y=BUDGET,
            hue=WORLDWIDE,
            size=WORLDWIDE,
            ax=ax,
        )
    ax.set(ylabel="Budget in $ millions", xlabel="Year")
    return fig


def decade_chart(data: pd.DataFrame) -> Figure:
    """Bar chart of the number of films released per decade."""
    counts = films_per_decade(data)
    fig = _new_figure()
    ax = fig.add_subplot()
    ax.bar([str(decade) for decade in counts.index], counts.to_numpy())
    ax.set(xlabel="Decade", ylabel="Number of films")
    return fig


def _draw_regression(
    ax: Axes,
    films: pd.DataFrame,
    *,
    dot_colour: str | None,
    line_colour: str,
    title: str,
) -> None:
    is_styled = dot_colour is not None
    with sns.axes_style("darkgrid" if is_styled else "whitegrid"):
        sns.regplot(
            data=films,
            x=BUDGET,
            y=WORLDWIDE,
            color=dot_colour,
            scatter_kws={"alpha": 0.4},
            line_kws={"color": line_colour},
            ax=ax,
        )
    ax.set_title(title)
    if is_styled:
        ax.set(
            ylim=(0, None),
            xlim=(0, None),
            ylabel="Revenue in $ billions",
            xlabel="Budget in $ millions",
        )


def regression_chart(
    films: pd.DataFrame,
    *,
    dot_colour: str | None = None,
    line_colour: str = "black",
    title: str = "",
) -> Figure:
    """Scatter plot of budget against gross with the fitted regression line."""
    fig = _new_figure()
    _draw_regression(
        fig.add_subplot(),
        films,
        dot_colour=dot_colour,
        line_colour=line_colour,
        title=title,
    )
    return fig


def regression_comparison_chart(old: pd.DataFrame, new: pd.DataFrame) -> Figure:
    """Old films (default style) and new films (styled) side by side."""
    fig = Figure(figsize=COMPARISON_SIZE, dpi=FIGURE_DPI)
    old_ax, new_ax = fig.subplots(1, 2)
    _draw_regression(
        old_ax, old, dot_colour=None, line_colour="black", title="Films before 1970"
    )
    _draw_regression(
        new_ax,
        new,
        dot_colour=NEW_FILMS_DOT_COLOUR,
        line_colour=NEW_FILMS_LINE_COLOUR,
        title="Films from 1970",
    )
    fig.tight_layout()
    return fig


def fitted_line_chart(films: pd.DataFrame, result: RegressionResult) -> Figure:
    """Scatter plot with the line drawn from the scikit-learn estimates."""
    fig = _new_figure()
    ax = fig.add_subplot()
    with sns.axes_style("darkgrid"):
        ax.scatter(
            films[BUDGET], films[WORLDWIDE], alpha=0.4, color=NEW_FILMS_DOT_COLOUR
        )
    budgets = [0.0, float(films[BUDGET].max())]
    ax.plot(
        budgets,
        [result.predict(budget) for budget in budgets],
        color=NEW_FILMS_LINE_COLOUR,
        linewidth=2,
    )
    ax.set(
        ylim=(0, None),
        xlim=(0, None),
        ylabel="Revenue in $ billions",
        xlabel="Budget in $ millions",
    )
    ax.text(
        0.03,
        0.95,
        f"Intercept: {result.intercept:,.0f}\n"
        f"Slope: {result.slope:.4f}\n"
        f"R-squared: {result.r_squared:.4f}",
        transform=ax.transAxes,
        va="top",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.9},
    )
    return fig


def table_figure(frame: pd.DataFrame, title: str) -> Figure:
    """Render a small DataFrame as a table image sized to its text."""
    cells = frame.reset_index()
    text = cells.astype(str)
    characters = sum(
        max(len(str(name)), *(len(value) for value in text[name]))
        for name in cells.columns
    )
    width = max(FIGURE_SIZE[0], TABLE_INCHES_PER_CHARACTER * characters + 0.5)
    fig = Figure(figsize=(width, 0.8 + TABLE_ROW_INCHES * (len(frame) + 1)))
    ax = fig.add_subplot()
    ax.axis("off")
    ax.set_title(title)
    table = ax.table(
        cellText=text.to_numpy().tolist(),
        colLabels=[str(name) for name in cells.columns],
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(TABLE_FONT_SIZE)
    table.auto_set_column_width(list(range(len(cells.columns))))
    table.scale(1, 1.5)
    return fig
