**English** · [Dansk](Step-4-International-Releases-da) · [Bahasa Malaysia](Step-4-International-Releases-ms)

# Step 4: Filter on multiple conditions

**Question:** Which films earned nothing in the United States but something abroad, and which films were not released yet?

![Step 4: Filter on multiple conditions](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-4-international-releases.png)

## What the code does

`international_releases` combines two conditions with `.loc[]` and the bitwise `&`; each comparison needs its own parentheses because `&` binds tighter than `==`. `international_releases_query` writes the same filter as a string for `.query()` using the word `and`. Both find **155** films. `unreleased_films` finds **7** films released after 1 May 2018, and `remove_unreleased` returns `data_clean` with **5,384** films. **37.3 %** of these films did not earn back their budget (`share_losing_money`).

## What you gained

- Combining conditions with `&` and parentheses in `.loc[]`.
- The same filter as a readable string with `.query('a == 0 and b != 0')`.
- Removing rows with `.drop(index)` and keeping a clean copy for the rest of the analysis.

Previous: [Step 3: Films with zero revenue](Step-3-Zero-Revenue) · Next: [Step 5: Seaborn bubble charts](Step-5-Bubble-Chart)
