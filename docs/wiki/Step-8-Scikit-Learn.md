**English** · [Dansk](Step-8-Scikit-Learn-da) · [Bahasa Malaysia](Step-8-Scikit-Learn-ms)

# Step 8: Run your own regression with scikit-learn

**Question:** What are the intercept and the slope of the line, and how good is the fit?

![Step 8: Run your own regression with scikit-learn](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn_and_Linear_Regression/raw/branch/main/docs/images/step-8-scikit-learn.png)

## What the code does

`fit_budget_to_revenue` creates a `LinearRegression`, passes the budget as the feature `X` and the worldwide gross as the target `y`, calls `.fit()` and reads `intercept_` (theta zero), `coef_` (theta one) and `.score()` (R-squared). **Old films:** intercept $22.8 million, slope 1.65, R-squared **0.029**: the budget explains about 3 % of the revenue. **New films:** intercept -$8.65 million, slope 3.12, R-squared **0.558**: every extra budget dollar goes with about $3.12 of revenue, and the line predicts about **$460 million** for a $150 million film.

## What you gained

- The `LinearRegression` workflow: create, `.fit(X, y)`, read `intercept_` and `coef_`.
- The features are named `X` (a DataFrame) and the target `y`.
- R-squared tells how much of the variation the line explains; 0.03 is poor, 0.56 is decent.

Previous: [Step 7: Regression plots with Seaborn](Step-7-Regression-Plots) · Next: [Step 9: Learning points and summary](Step-9-Summary)
