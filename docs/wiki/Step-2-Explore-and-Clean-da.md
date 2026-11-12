[English](Step-2-Explore-and-Clean) · **Dansk** · [Bahasa Malaysia](Step-2-Explore-and-Clean-ms)

# Trin 2: Udforsk og rens data

**Spørgsmål:** Hvordan er data opbygget, og hvordan gør vi pengekolonnerne numeriske?

![Trin 2: Udforsk og rens data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-2-explore-and-clean.png)

## Hvad koden gør

`describe_structure` finder **5.391 rækker og 6 kolonner, ingen NaN-værdier og ingen dubletter**. `convert_money_to_numbers` fjerner `$` og `,` med en indlejret løkke over de tre pengekolonner, og `convert_release_date` gør `Release_Date` til en datetime. `summary_statistics` (`.describe()`) viser et gennemsnitligt budget på ca. **31 mio. dollar** og en gennemsnitlig verdensomsætning på ca. **89 mio. dollar**; det højeste budget er 425.000.000 og den højeste verdensomsætning er 2.783.918.982. Den billigste film, *My Date With Drew*, kostede 1.100 dollar og indtjente 181.041.

## Hvad du fik ud af det

- `.shape`, `.head()`, `.info()`, `.isna()` og `.duplicated()` som de faste første kontroller.
- Rensning af tekst med `.str.replace()` i en indlejret løkke og derefter `pd.to_numeric`.
- `pd.to_datetime` til datoer og `.describe()` til hurtigt at få en fornemmelse for tallene.

Forrige: [Trin 1: Målene](Step-1-Goals-da) · Næste: [Trin 3: Film uden omsætning](Step-3-Zero-Revenue-da)
