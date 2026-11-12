**English** · [Dansk](Step-3-Zero-Revenue-da) · [Bahasa Malaysia](Step-3-Zero-Revenue-ms)

# Step 3: Films with zero revenue

**Question:** How many films earned nothing, and which expensive films were the biggest flops?

![Step 3: Films with zero revenue](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn_and_Linear_Regression/raw/branch/main/docs/images/step-3-zero-revenue.png)

## What the code does

`zero_domestic_films` finds **512** films with $0 in the United States and `zero_worldwide_films` finds **357** films with $0 worldwide, both sorted with the highest budget first. The top of the list (*Singularity*, *Aquaman*, *A Wrinkle in Time*) are films that had not been released yet when the data was collected, which the next step deals with.

## What you gained

- Filtering rows with a condition: `data[data.USD_Worldwide_Gross == 0]`.
- `.sort_values(..., ascending=False)` to see the largest first.
- A surprising result is a prompt to look closer at the data, not a result to trust.

Previous: [Step 2: Explore and clean the data](Step-2-Explore-and-Clean) · Next: [Step 4: Filter on multiple conditions](Step-4-International-Releases)
