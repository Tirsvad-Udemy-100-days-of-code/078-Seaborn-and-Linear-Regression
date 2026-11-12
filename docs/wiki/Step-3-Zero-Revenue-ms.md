[English](Step-3-Zero-Revenue) · [Dansk](Step-3-Zero-Revenue-da) · **Bahasa Malaysia**

# Langkah 3: Filem tanpa hasil

**Soalan:** Berapa banyak filem yang tidak memperoleh apa-apa, dan filem mahal yang manakah kegagalan terbesar?

![Langkah 3: Filem tanpa hasil](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-3-zero-revenue.png)

## Apa yang dilakukan kod

`zero_domestic_films` mendapati **512** filem dengan $0 di Amerika Syarikat dan `zero_worldwide_films` mendapati **357** filem dengan $0 di seluruh dunia, kedua-duanya disusun dengan bajet tertinggi dahulu. Bahagian atas senarai (*Singularity*, *Aquaman*, *A Wrinkle in Time*) ialah filem yang belum ditayangkan ketika data dikumpulkan, yang ditangani oleh langkah seterusnya.

## Apa yang anda perolehi

- Menapis baris dengan syarat: `data[data.USD_Worldwide_Gross == 0]`.
- `.sort_values(..., ascending=False)` untuk melihat yang terbesar dahulu.
- Keputusan yang mengejutkan ialah isyarat untuk menyemak data dengan lebih teliti, bukan keputusan untuk dipercayai.

Sebelumnya: [Langkah 2: Teroka dan bersihkan data](Step-2-Explore-and-Clean-ms) · Seterusnya: [Langkah 4: Tapis pada berbilang syarat](Step-4-International-Releases-ms)
