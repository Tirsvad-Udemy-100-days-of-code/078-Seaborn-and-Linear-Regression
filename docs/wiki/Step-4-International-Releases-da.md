[English](Step-4-International-Releases) · **Dansk** · [Bahasa Malaysia](Step-4-International-Releases-ms)

# Trin 4: Filtrér på flere betingelser

**Spørgsmål:** Hvilke film indtjente ingenting i USA, men noget i udlandet, og hvilke film var ikke udkommet endnu?

![Trin 4: Filtrér på flere betingelser](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-4-international-releases.png)

## Hvad koden gør

`international_releases` kombinerer to betingelser med `.loc[]` og den bitvise `&`; hver sammenligning skal have sin egen parentes, fordi `&` binder stærkere end `==`. `international_releases_query` skriver det samme filter som en streng til `.query()` med ordet `and`. Begge finder **155** film. `unreleased_films` finder **7** film udgivet efter 1. maj 2018, og `remove_unreleased` returnerer `data_clean` med **5.384** film. **37,3 %** af filmene tjente ikke deres budget ind igen (`share_losing_money`).

## Hvad du fik ud af det

- At kombinere betingelser med `&` og parenteser i `.loc[]`.
- Det samme filter som en læsbar streng med `.query('a == 0 and b != 0')`.
- At fjerne rækker med `.drop(index)` og beholde en ren kopi til resten af analysen.

Forrige: [Trin 3: Film uden omsætning](Step-3-Zero-Revenue-da) · Næste: [Trin 5: Seaborn-boblediagrammer](Step-5-Bubble-Chart-da)
