[English](Step-3-Zero-Revenue) · **Dansk** · [Bahasa Malaysia](Step-3-Zero-Revenue-ms)

# Trin 3: Film uden omsætning

**Spørgsmål:** Hvor mange film indtjente ingenting, og hvilke dyre film var de største flop?

![Trin 3: Film uden omsætning](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-3-zero-revenue.png)

## Hvad koden gør

`zero_domestic_films` finder **512** film med 0 dollar i USA, og `zero_worldwide_films` finder **357** film med 0 dollar i hele verden, begge sorteret med det højeste budget først. Toppen af listen (*Singularity*, *Aquaman*, *A Wrinkle in Time*) er film, der ikke var udkommet endnu, da data blev indsamlet, hvilket næste trin tager hånd om.

## Hvad du fik ud af det

- At filtrere rækker med en betingelse: `data[data.USD_Worldwide_Gross == 0]`.
- `.sort_values(..., ascending=False)` for at se de største først.
- Et overraskende resultat er en opfordring til at se nærmere på data, ikke et resultat, man skal stole på.

Forrige: [Trin 2: Udforsk og rens data](Step-2-Explore-and-Clean-da) · Næste: [Trin 4: Filtrér på flere betingelser](Step-4-International-Releases-da)
