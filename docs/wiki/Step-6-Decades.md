**English** · [Dansk](Step-6-Decades-da) · [Bahasa Malaysia](Step-6-Decades-ms)

# Step 6: Floor division to convert years to decades

**Question:** How do we group films by decade?

![Step 6: Floor division to convert years to decades](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn_and_Linear_Regression/raw/branch/main/docs/images/step-6-decades.png)

## What the code does

`add_decade` makes a `DatetimeIndex` from `Release_Date`, takes its `.year` and applies floor division: `year // 10 * 10`, so 1992 and 1999 both become **1990**. The rule lives once in `to_decade` in the domain layer. `split_old_and_new` then separates the **153** old films (before 1970) from the **5,231** new films, and `decade_chart` counts the films per decade: the industry grew explosively after 1970.

## What you gained

- `//` (floor division) drops the remainder: `1999 // 10 * 10 == 1990`.
- `pd.DatetimeIndex(column).year` pulls the years out of dates.
- Adding a derived column to group, count and split a DataFrame.

Previous: [Step 5: Seaborn bubble charts](Step-5-Bubble-Chart) · Next: [Step 7: Regression plots with Seaborn](Step-7-Regression-Plots)
