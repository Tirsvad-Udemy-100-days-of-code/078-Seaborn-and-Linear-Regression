**English** · [Dansk](Step-7-Regression-Plots-da) · [Bahasa Malaysia](Step-7-Regression-Plots-ms)

# Step 7: Regression plots with Seaborn

**Question:** Does a straight line describe how budget leads to revenue?

![Step 7: Regression plots with Seaborn](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn_and_Linear_Regression/raw/branch/main/docs/images/step-7-regression-plots.png)

## What the code does

`regression_chart` calls `sns.regplot`, which draws the scatter plot, the linear regression line and its confidence interval in one call. For the **old films** the points lie far from the line: budget says little about revenue. For the **new films** the points follow the line much better. Styling goes through `scatter_kws` (for example `alpha`) and `line_kws` (for example the colour); the new-films chart uses dark blue dots (`#2f4b7c`), an orange line (`#ff7c43`), a `darkgrid` and axes that do not show negative values.

## What you gained

- `sns.regplot` shows data and regression line together.
- `scatter_kws` and `line_kws` take dictionaries for the dots and the line.
- Judging a regression by eye: how close are the points to the line?

Previous: [Step 6: Floor division to convert years to decades](Step-6-Decades) · Next: [Step 8: Run your own regression with scikit-learn](Step-8-Scikit-Learn)
