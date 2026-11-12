**English** · [Dansk](Step-5-Bubble-Chart-da) · [Bahasa Malaysia](Step-5-Bubble-Chart-ms)

# Step 5: Seaborn bubble charts

**Question:** How do budget and revenue relate, and how has the film industry changed?

![Step 5: Seaborn bubble charts](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-5-bubble-chart.png)

## What the code does

`bubble_chart` calls `sns.scatterplot` with the budget on the x axis and the worldwide gross on the y axis. Giving `hue` and `size` the worldwide gross turns the scatter plot into a **bubble chart** with a third dimension. A `darkgrid` style, axis limits and the labels "Budget in $100 millions" and "Revenue in $ billions" are set on the Matplotlib axes. `bubble_chart_by_date` puts the release date on the x axis to show how budgets exploded over the decades.

## What you gained

- Seaborn is built on Matplotlib: you can always drop to the Matplotlib layer with `ax.set(...)`.
- `sns.scatterplot(hue=..., size=...)` adds a third and fourth dimension to a chart.
- `with sns.axes_style('darkgrid'):` styles a chart without changing the global style.

Previous: [Step 4: Filter on multiple conditions](Step-4-International-Releases) · Next: [Step 6: Floor division to convert years to decades](Step-6-Decades)
