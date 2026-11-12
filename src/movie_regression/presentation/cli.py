"""Command line: load the data, build the report and print it."""

from movie_regression.application.report import build_report
from movie_regression.infrastructure.data import load_films


def main() -> None:
    """Print the report for the bundled data set."""
    print(build_report(load_films()), end="")
