**English** · [Dansk](Step-2-Explore-and-Clean-da) · [Bahasa Malaysia](Step-2-Explore-and-Clean-ms)

# Step 2: Explore and clean the data

**Question:** How is the data structured, and how do we make the money columns numeric?

![Step 2: Explore and clean the data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn_and_Linear_Regression/raw/branch/main/docs/images/step-2-explore-and-clean.png)

## What the code does

`describe_structure` finds **5,391 rows and 6 columns, no NaN values and no duplicates**. `convert_money_to_numbers` removes `$` and `,` with a nested loop over the three money columns, and `convert_release_date` makes `Release_Date` a datetime. `summary_statistics` (`.describe()`) shows a mean budget of about **$31 million** and a mean worldwide gross of about **$89 million**; the highest budget is $425,000,000 and the highest worldwide gross is $2,783,918,982. The cheapest film, *My Date With Drew*, cost $1,100 and earned $181,041.

## What you gained

- `.shape`, `.head()`, `.info()`, `.isna()` and `.duplicated()` as the standard first checks.
- Cleaning text with `.str.replace()` inside a nested loop, then `pd.to_numeric`.
- `pd.to_datetime` for dates, and `.describe()` for a quick feel of the numbers.

Previous: [Step 1: The goals](Step-1-Goals) · Next: [Step 3: Films with zero revenue](Step-3-Zero-Revenue)
