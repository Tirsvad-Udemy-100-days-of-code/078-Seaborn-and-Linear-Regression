[English](Step-8-Scikit-Learn) · **Dansk** · [Bahasa Malaysia](Step-8-Scikit-Learn-ms)

# Trin 8: Kør din egen regression med scikit-learn

**Spørgsmål:** Hvad er linjens skæring og hældning, og hvor god er tilpasningen?

![Trin 8: Kør din egen regression med scikit-learn](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-8-scikit-learn.png)

## Hvad koden gør

`fit_budget_to_revenue` opretter en `LinearRegression`, giver budgettet som feature `X` og verdensomsætningen som mål `y`, kalder `.fit()` og aflæser `intercept_` (theta nul), `coef_` (theta ét) og `.score()` (R-i-anden). **Gamle film:** skæring 22,8 mio. dollar, hældning 1,65, R-i-anden **0,029**: budgettet forklarer ca. 3 % af omsætningen. **Nye film:** skæring -8,65 mio. dollar, hældning 3,12, R-i-anden **0,558**: hver ekstra budgetdollar følges af ca. 3,12 dollar i omsætning, og linjen forudsiger ca. **460 mio. dollar** for en film til 150 mio. dollar.

## Hvad du fik ud af det

- `LinearRegression`-forløbet: opret, `.fit(X, y)`, aflæs `intercept_` og `coef_`.
- Features hedder `X` (en DataFrame) og målet `y`.
- R-i-anden fortæller, hvor meget af variationen linjen forklarer; 0,03 er dårligt, 0,56 er ganske fint.

Forrige: [Trin 7: Regressionsplot med Seaborn](Step-7-Regression-Plots-da) · Næste: [Trin 9: Læringspunkter og opsummering](Step-9-Summary-da)
