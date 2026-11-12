[English](Step-6-Decades) · **Dansk** · [Bahasa Malaysia](Step-6-Decades-ms)

# Trin 6: Heltalsdivision til at omregne år til årtier

**Spørgsmål:** Hvordan grupperer vi film efter årti?

![Trin 6: Heltalsdivision til at omregne år til årtier](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-6-decades.png)

## Hvad koden gør

`add_decade` laver et `DatetimeIndex` af `Release_Date`, tager dets `.year` og anvender heltalsdivision: `year // 10 * 10`, så både 1992 og 1999 bliver til **1990**. Reglen findes kun ét sted, i `to_decade` i domænelaget. `split_old_and_new` skiller derefter de **153** gamle film (før 1970) fra de **5.231** nye film, og `decade_chart` tæller filmene pr. årti: industrien voksede eksplosivt efter 1970.

## Hvad du fik ud af det

- `//` (heltalsdivision) smider resten væk: `1999 // 10 * 10 == 1990`.
- `pd.DatetimeIndex(kolonne).year` henter årstallene ud af datoerne.
- At tilføje en afledt kolonne for at gruppere, tælle og opdele en DataFrame.

Forrige: [Trin 5: Seaborn-boblediagrammer](Step-5-Bubble-Chart-da) · Næste: [Trin 7: Regressionsplot med Seaborn](Step-7-Regression-Plots-da)
