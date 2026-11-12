import pandas as pd

from movie_regression.application.report import build_report


def test_build_report_lists_the_lecture_answers(raw_films: pd.DataFrame) -> None:
    report = build_report(raw_films)

    assert "Rows: 5391, columns: 6" in report
    assert "International releases: 155 (query: 155)" in report
    assert "predicted revenue for a $150,000,000 budget" in report
