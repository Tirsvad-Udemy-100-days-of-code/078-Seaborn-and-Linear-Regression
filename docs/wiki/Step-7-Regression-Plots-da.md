[English](Step-7-Regression-Plots) · **Dansk** · [Bahasa Malaysia](Step-7-Regression-Plots-ms)

# Trin 7: Regressionsplot med Seaborn

**Spørgsmål:** Beskriver en ret linje, hvordan budget fører til omsætning?

![Trin 7: Regressionsplot med Seaborn](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-7-regression-plots.png)

## Hvad koden gør

`regression_chart` kalder `sns.regplot`, der tegner punktdiagrammet, den lineære regressionslinje og dens konfidensinterval i ét kald. For de **gamle film** ligger punkterne langt fra linjen: budgettet siger kun lidt om omsætningen. For de **nye film** følger punkterne linjen meget bedre. Stilen sættes med `scatter_kws` (fx `alpha`) og `line_kws` (fx farven); diagrammet for de nye film bruger mørkeblå prikker (`#2f4b7c`), en orange linje (`#ff7c43`), et `darkgrid` og akser, der ikke viser negative værdier.

## Hvad du fik ud af det

- `sns.regplot` viser data og regressionslinje sammen.
- `scatter_kws` og `line_kws` tager ordbøger til prikkerne og linjen.
- At bedømme en regression med øjet: hvor tæt ligger punkterne på linjen?

Forrige: [Trin 6: Heltalsdivision til at omregne år til årtier](Step-6-Decades-da) · Næste: [Trin 8: Kør din egen regression med scikit-learn](Step-8-Scikit-Learn-da)
