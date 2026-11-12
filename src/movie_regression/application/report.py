"""Answer the questions of the lecture as plain text."""

import pandas as pd

from movie_regression.application import analysis, cleaning
from movie_regression.application.regression import (
    RegressionResult,
    fit_budget_to_revenue,
)
from movie_regression.domain.rules import BUDGET, WORLDWIDE

PREDICTION_BUDGET = 150_000_000
TOP_FLOPS = 3


def _regression_lines(label: str, films: pd.DataFrame) -> list[str]:
    result: RegressionResult = fit_budget_to_revenue(films)
    return [
        f"{label} films: {len(films)}",
        f"  intercept {result.intercept:,.0f}, slope {result.slope:.4f}, "
        f"R-squared {result.r_squared:.4f}",
        f"  predicted revenue for a ${PREDICTION_BUDGET:,} budget: "
        f"${result.predict(PREDICTION_BUDGET):,.0f}",
    ]


def _stat(stats: pd.DataFrame, name: str, column: str) -> float:
    """One number of the describe() table, as a float."""
    return float(stats[column].astype("float64")[name])


def build_report(raw: pd.DataFrame) -> str:
    """Return a plain-text report with the answer of every lecture step."""
    structure = cleaning.describe_structure(raw)
    films = cleaning.prepare(raw)
    clean = cleaning.remove_unreleased(films)
    stats = analysis.summary_statistics(films)
    flops = analysis.zero_worldwide_films(films).head(TOP_FLOPS)
    old, new = analysis.split_old_and_new(films)
    clean_old, clean_new = analysis.split_old_and_new(clean)

    lines = [
        "Movie budget and revenue",
        f"Rows: {structure.rows}, columns: {structure.columns}, "
        f"NaN values: {structure.has_nan}, duplicates: {structure.duplicate_rows}",
        f"Mean budget: ${_stat(stats, 'mean', BUDGET):,.0f}, "
        f"mean worldwide gross: ${_stat(stats, 'mean', WORLDWIDE):,.0f}",
        f"Highest budget: ${_stat(stats, 'max', BUDGET):,.0f}, "
        f"highest worldwide gross: ${_stat(stats, 'max', WORLDWIDE):,.0f}",
        f"Films with zero domestic gross: {len(analysis.zero_domestic_films(films))}",
        f"Films with zero worldwide gross: {len(analysis.zero_worldwide_films(films))}",
        "Biggest flops: " + ", ".join(flops["Movie_Title"]),
        f"International releases: {len(analysis.international_releases(films))} "
        f"(query: {len(analysis.international_releases_query(films))})",
        f"Unreleased films: {len(cleaning.unreleased_films(films))}",
        f"Films losing money: {analysis.share_losing_money(clean):.1f}%",
        f"Old films before 1970 (all data): {len(old)}, new films: {len(new)}",
        f"Old films before 1970 (released only): {len(clean_old)}, "
        f"new films: {len(clean_new)}",
        *_regression_lines("Old", clean_old),
        *_regression_lines("New", clean_new),
    ]
    return "\n".join(lines) + "\n"
