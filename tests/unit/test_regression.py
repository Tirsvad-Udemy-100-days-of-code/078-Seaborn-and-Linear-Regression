import pandas as pd
import pytest

from movie_regression.application.regression import fit_budget_to_revenue


def test_fit_recovers_an_exact_line() -> None:
    films = pd.DataFrame(
        {
            "USD_Production_Budget": [1.0, 2.0, 3.0],
            "USD_Worldwide_Gross": [5.0, 7.0, 9.0],
        }
    )

    result = fit_budget_to_revenue(films)

    assert result.intercept == pytest.approx(3.0)
    assert result.slope == pytest.approx(2.0)
    assert result.r_squared == pytest.approx(1.0)
    assert result.predict(10) == pytest.approx(23.0)
