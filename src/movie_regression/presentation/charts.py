"""Presentation: the charts of the lecture as matplotlib figures.

Figures are built without pyplot, so no global state is shared between tests.
"""

from pathlib import Path

import pandas as pd
import seaborn as sns
from matplotlib.figure import Figure

from movie_regression.application.analysis import films_per_decade
from movie_regression.domain.rules import BUDGET, RELEASE_DATE, WORLDWIDE

FIGURE_SIZE = (8, 4)
FIGURE_DPI = 200
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


def regression_chart(
    films: pd.DataFrame,
    *,
    dot_colour: str | None = None,
    line_colour: str = "black",
    title: str = "",
) -> Figure:
    """Scatter plot of budget against gross with the fitted regression line."""
    is_styled = dot_colour is not None
    fig = _new_figure()
    ax = fig.add_subplot()
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
    return fig


def table_figure(frame: pd.DataFrame, title: str) -> Figure:
    """Render a small DataFrame as a table image."""
    fig = Figure(figsize=(FIGURE_SIZE[0], 0.5 + 0.4 * (len(frame) + 1)))
    ax = fig.add_subplot()
    ax.axis("off")
    ax.set_title(title)
    cells = frame.reset_index()
    table = ax.table(
        cellText=cells.astype(str).to_numpy(),
        colLabels=[str(name) for name in cells.columns],
        loc="center",
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    return fig
