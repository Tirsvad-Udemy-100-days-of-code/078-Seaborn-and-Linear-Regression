"""Render one screenshot per lecture step into docs/images/.

Tables and charts are drawn from the package, without a display. Usage:
    python scripts/make_screenshots.py [output_dir]
"""

from __future__ import annotations

import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import pandas as pd  # noqa: E402
from matplotlib.figure import Figure  # noqa: E402

from movie_regression.application import analysis, cleaning  # noqa: E402
from movie_regression.application.regression import (  # noqa: E402
    RegressionResult,
    fit_budget_to_revenue,
)
from movie_regression.application.report import PREDICTION_BUDGET  # noqa: E402
from movie_regression.domain.rules import MONEY_COLUMNS, RELEASE_DATE  # noqa: E402
from movie_regression.infrastructure.data import load_films  # noqa: E402
from movie_regression.presentation import charts  # noqa: E402

DEFAULT_OUT = Path(__file__).resolve().parents[1] / "docs" / "images"
TABLE_ROWS = 10


def _money(value: float) -> str:
    return f"{value:,.0f}"


def readable(frame: pd.DataFrame) -> pd.DataFrame:
    """Copy of a film table with thousands separators and plain dates."""
    shown = frame.copy()
    for column in MONEY_COLUMNS:
        if column in shown.columns:
            shown[column] = shown[column].map(_money)
    if RELEASE_DATE in shown.columns:
        shown[RELEASE_DATE] = pd.to_datetime(shown[RELEASE_DATE]).dt.strftime(
            "%Y-%m-%d"
        )
    return shown


def describe_table(films: pd.DataFrame) -> pd.DataFrame:
    """`describe()` with every number written with thousands separators."""
    numbers = films.select_dtypes("number")
    return analysis.summary_statistics(numbers).map(_money).rename_axis("Statistic")


def summary_table(old: pd.DataFrame, new: pd.DataFrame) -> pd.DataFrame:
    """Old against new films: size, estimates and a prediction."""
    rows: dict[str, list[str]] = {}
    for label, films in (("Old films (before 1970)", old), ("New films (1970+)", new)):
        result: RegressionResult = fit_budget_to_revenue(films)
        rows[label] = [
            str(len(films)),
            _money(result.intercept),
            f"{result.slope:.4f}",
            f"{result.r_squared:.4f}",
            _money(result.predict(PREDICTION_BUDGET)),
        ]
    return pd.DataFrame.from_dict(
        rows,
        orient="index",
        columns=[
            "Films",
            "Intercept",
            "Slope",
            "R-squared",
            f"Revenue for ${PREDICTION_BUDGET // 1_000_000} million budget",
        ],
    ).rename_axis("Group")


def build_steps() -> dict[str, Figure]:
    """Build the nine step figures, keyed by file name."""
    raw = load_films()
    films = cleaning.prepare(raw)
    clean = cleaning.remove_unreleased(films)
    old, new = analysis.split_old_and_new(clean)
    international = analysis.international_releases(films)
    flops = analysis.zero_worldwide_films(films).head(TABLE_ROWS)

    return {
        "step-1-goals.png": charts.table_figure(
            raw.head(TABLE_ROWS),
            "Step 1: the question - do higher budgets lead to more revenue?",
        ),
        "step-2-explore-and-clean.png": charts.table_figure(
            describe_table(films),
            "Step 2: explore and clean - describe() of the cleaned data",
        ),
        "step-3-zero-revenue.png": charts.table_figure(
            readable(flops.drop(columns="Rank")),
            "Step 3: the 10 dearest films with zero worldwide gross",
        ),
        "step-4-international-releases.png": charts.table_figure(
            readable(international.head(TABLE_ROWS).drop(columns="Rank")),
            f"Step 4: international releases ({len(international)} films), "
            f"first {TABLE_ROWS}",
        ),
        "step-5-bubble-chart.png": charts.bubble_chart(clean),
        "step-6-decades.png": charts.decade_chart(clean),
        "step-7-regression-plots.png": charts.regression_comparison_chart(old, new),
        "step-8-scikit-learn.png": charts.fitted_line_chart(
            new, fit_budget_to_revenue(new)
        ),
        "step-9-summary.png": charts.table_figure(
            summary_table(old, new), "Step 9: summary"
        ),
    }


def main(out_dir: Path) -> None:
    """Write every step image to out_dir."""
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, fig in build_steps().items():
        charts.save_figure(fig, out_dir / name)
        print(f"wrote {out_dir / name}")


if __name__ == "__main__":
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT)
