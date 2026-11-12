[English](Step-8-Scikit-Learn) · [Dansk](Step-8-Scikit-Learn-da) · **Bahasa Malaysia**

# Langkah 8: Jalankan regresi anda sendiri dengan scikit-learn

**Soalan:** Apakah pintasan dan kecerunan garis itu, dan sebaik manakah padanannya?

![Langkah 8: Jalankan regresi anda sendiri dengan scikit-learn](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-8-scikit-learn.png)

## Apa yang dilakukan kod

`fit_budget_to_revenue` mencipta `LinearRegression`, memberikan bajet sebagai ciri `X` dan hasil seluruh dunia sebagai sasaran `y`, memanggil `.fit()` dan membaca `intercept_` (theta sifar), `coef_` (theta satu) dan `.score()` (R-kuasa dua). **Filem lama:** pintasan $22.8 juta, kecerunan 1.65, R-kuasa dua **0.029**: bajet menerangkan kira-kira 3 % hasil. **Filem baharu:** pintasan -$8.65 juta, kecerunan 3.12, R-kuasa dua **0.558**: setiap dolar bajet tambahan disertai kira-kira $3.12 hasil, dan garis itu meramalkan kira-kira **$460 juta** untuk filem berbajet $150 juta.

## Apa yang anda perolehi

- Aliran kerja `LinearRegression`: cipta, `.fit(X, y)`, baca `intercept_` dan `coef_`.
- Ciri dinamakan `X` (DataFrame) dan sasaran `y`.
- R-kuasa dua menunjukkan berapa banyak variasi yang diterangkan garis; 0.03 lemah, 0.56 agak baik.

Sebelumnya: [Langkah 7: Plot regresi dengan Seaborn](Step-7-Regression-Plots-ms) · Seterusnya: [Langkah 9: Pelajaran dan ringkasan](Step-9-Summary-ms)
