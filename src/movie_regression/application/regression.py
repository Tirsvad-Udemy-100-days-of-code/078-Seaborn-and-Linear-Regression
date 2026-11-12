"""Lecture step 8: a linear regression of revenue on budget."""

from dataclasses import dataclass

import pandas as pd
from sklearn.linear_model import LinearRegression

from movie_regression.domain.rules import BUDGET, WORLDWIDE


@dataclass(frozen=True)
class RegressionResult:
    """The estimates of the line  revenue = intercept + slope * budget."""

    intercept: float
    slope: float
    r_squared: float

    def predict(self, budget: float) -> float:
        """Revenue the line predicts for a production budget."""
        return self.intercept + self.slope * budget


def fit_budget_to_revenue(films: pd.DataFrame) -> RegressionResult:
    """Fit worldwide gross against production budget with scikit-learn."""
    features = pd.DataFrame(films, columns=[BUDGET])
    target = pd.DataFrame(films, columns=[WORLDWIDE])
    model = LinearRegression().fit(features, target)
    return RegressionResult(
        intercept=float(model.intercept_[0]),
        slope=float(model.coef_[0][0]),
        r_squared=float(model.score(features, target)),
    )
