[English](Step-5-Bubble-Chart) · **Dansk** · [Bahasa Malaysia](Step-5-Bubble-Chart-ms)

# Trin 5: Seaborn-boblediagrammer

**Spørgsmål:** Hvordan hænger budget og omsætning sammen, og hvordan har filmindustrien ændret sig?

![Trin 5: Seaborn-boblediagrammer](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn_and_Linear_Regression/raw/branch/main/docs/images/step-5-bubble-chart.png)

## Hvad koden gør

`bubble_chart` kalder `sns.scatterplot` med budgettet på x-aksen og verdensomsætningen på y-aksen. Når `hue` og `size` er verdensomsætningen, bliver punktdiagrammet til et **boblediagram** med en tredje dimension. En `darkgrid`-stil, aksegrænser og teksterne "Budget in $100 millions" og "Revenue in $ billions" sættes på Matplotlib-aksen. `bubble_chart_by_date` sætter udgivelsesdatoen på x-aksen for at vise, hvordan budgetterne eksploderede gennem årtierne.

## Hvad du fik ud af det

- Seaborn er bygget oven på Matplotlib: du kan altid gå ned i Matplotlib-laget med `ax.set(...)`.
- `sns.scatterplot(hue=..., size=...)` tilføjer en tredje og fjerde dimension til et diagram.
- `with sns.axes_style('darkgrid'):` giver et diagram en stil uden at ændre den globale stil.

Forrige: [Trin 4: Filtrér på flere betingelser](Step-4-International-Releases-da) · Næste: [Trin 6: Heltalsdivision til at omregne år til årtier](Step-6-Decades-da)
