**English** · [Dansk](Step-1-Goals-da) · [Bahasa Malaysia](Step-1-Goals-ms)

# Step 1: The goals

**Question:** Do higher film budgets lead to more revenue at the box office?

![Step 1: The goals](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-1-goals.png)

## What the code does

`load_films` reads `cost_revenue_dirty.csv` into a DataFrame: 5,391 films with `Rank`, `Release_Date`, `Movie_Title`, `USD_Production_Budget`, `USD_Worldwide_Gross` and `USD_Domestic_Gross`. The money columns are still text such as `$110,000`, so they cannot be used in calculations yet.

## What you gained

- The question the day answers: should a studio spend more on a film to earn more?
- The tools of the day: Seaborn charts, bubble charts, floor division and a linear regression with scikit-learn.
- How a dirty CSV looks before it is cleaned: always look at the data first.

Previous: [Getting Started](Getting-Started) · Next: [Step 2: Explore and clean the data](Step-2-Explore-and-Clean)
