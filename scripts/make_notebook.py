"""Build notebooks/Seaborn_and_Linear_Regression.ipynb (without outputs).

Run the notebook afterwards to store the outputs:
    python scripts/make_notebook.py
    python -m jupyter nbconvert --to notebook --execute --inplace
        notebooks/Seaborn_and_Linear_Regression.ipynb
"""

from __future__ import annotations

from pathlib import Path

import nbformat
from nbformat.v4 import new_code_cell, new_markdown_cell, new_notebook

NOTEBOOK = (
    Path(__file__).resolve().parents[1]
    / "notebooks"
    / "Seaborn_and_Linear_Regression.ipynb"
)

INTRO = """# Movie budget and revenue: Seaborn and linear regression

Day 78 of Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*.

**The question:** do films with a higher production budget earn more money?

**What you learn:** cleaning money columns with pandas, filtering and
grouping films, Seaborn scatter and bubble charts, `regplot`, and a linear
regression with scikit-learn (intercept, slope and R-squared).

The code lives in the `movie_regression` package; the notebook calls it step
by step."""

STEPS: list[tuple[str, str, str]] = [
    (
        "## Step 1: Project goals and the data",
        "Load the raw file. The money columns are still text such as "
        "`$110,000`, so pandas cannot calculate with them yet.",
        """%matplotlib inline
from IPython.display import display

from movie_regression.application import analysis, cleaning
from movie_regression.application.regression import fit_budget_to_revenue
from movie_regression.application.report import PREDICTION_BUDGET
from movie_regression.infrastructure.data import DATA_FILE, load_films
from movie_regression.presentation import charts

raw = load_films(DATA_FILE)
display(raw.head())
raw.shape""",
    ),
    (
        "## Step 2: Explore and clean the data",
        "Check rows, NaN values and duplicates, then turn the money columns "
        "into numbers and `Release_Date` into a date.",
        """structure = cleaning.describe_structure(raw)
print(structure)

films = cleaning.prepare(raw)
display(films.dtypes.to_frame("dtype"))
films.describe()""",
    ),
    (
        "## Step 3: Films with zero revenue",
        "The cheapest and dearest films, the films that earned nothing at "
        "all, and the films released after the data was collected "
        "(1 May 2018) that must be removed.",
        """display(analysis.lowest_budget_films(films))
display(analysis.highest_budget_films(films))
print("Zero domestic gross:", len(analysis.zero_domestic_films(films)))
zero_worldwide = analysis.zero_worldwide_films(films)
print("Zero worldwide gross:", len(zero_worldwide))
display(zero_worldwide.head(10))

print("Unreleased films:", len(cleaning.unreleased_films(films)))
clean = cleaning.remove_unreleased(films)
print(f"Films losing money: {analysis.share_losing_money(clean):.1f}%")""",
    ),
    (
        "## Step 4: International releases",
        "Zero domestic gross but some worldwide gross: filtered with "
        "`.loc[]` and `&`, and again with `.query()`.",
        """international = analysis.international_releases(films)
print(len(international), len(analysis.international_releases_query(films)))
international.head(10)""",
    ),
    (
        "## Step 5: Seaborn scatter and bubble charts",
        "Budget against worldwide gross: first a plain scatter plot, then a "
        "bubble chart where colour and size show the revenue.",
        """display(charts.scatter_chart(clean))
charts.bubble_chart(clean)""",
    ),
    (
        "## Step 6: Films per decade",
        "Floor division turns a year into a decade: 1992 and 1999 both become 1990.",
        """with_decade = analysis.add_decade(clean)
display(with_decade[["Release_Date", "Decade"]].head())
charts.decade_chart(clean)""",
    ),
    (
        "## Step 7: Regression plots with Seaborn",
        "Seaborn's `regplot` draws the points and a fitted line. Old films "
        "(before 1970) use the default style; new films get their own dot "
        "and line colours.",
        """old, new = analysis.split_old_and_new(clean)
print("Old films:", len(old), "New films:", len(new))
display(charts.regression_chart(old, title="Films before 1970"))
display(
    charts.regression_chart(
        new,
        dot_colour=charts.NEW_FILMS_DOT_COLOUR,
        line_colour=charts.NEW_FILMS_LINE_COLOUR,
        title="Films from 1970",
    )
)
charts.regression_comparison_chart(old, new)""",
    ),
    (
        "## Step 8: Linear regression with scikit-learn",
        "Fit `revenue = intercept + slope * budget` and draw the line from "
        "the estimates. R-squared tells how much of the variation in "
        "revenue the budget explains.",
        """new_result = fit_budget_to_revenue(new)
print(new_result)
charts.fitted_line_chart(new, new_result)""",
    ),
    (
        "## Step 9: Summary and prediction",
        "Compare old and new films and predict the revenue of a film with a "
        "$150 million budget.",
        """old_result = fit_budget_to_revenue(old)
for label, result in (("Old", old_result), ("New", new_result)):
    print(
        f"{label}: intercept {result.intercept:,.0f}, slope {result.slope:.4f}, "
        f"R-squared {result.r_squared:.4f}, "
        f"prediction for ${PREDICTION_BUDGET:,}: "
        f"${result.predict(PREDICTION_BUDGET):,.0f}"
    )""",
    ),
]


def build_notebook() -> nbformat.NotebookNode:
    """Assemble the notebook: an intro, then a heading, text and code per step."""
    cells = [new_markdown_cell(INTRO)]
    for heading, text, code in STEPS:
        cells.append(new_markdown_cell(f"{heading}\n\n{text}"))
        cells.append(new_code_cell(code))
    notebook = new_notebook(cells=cells)
    notebook.metadata["kernelspec"] = {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    }
    return notebook


def main() -> None:
    """Write the notebook file."""
    NOTEBOOK.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(build_notebook(), NOTEBOOK)
    print(f"wrote {NOTEBOOK}")


if __name__ == "__main__":
    main()
