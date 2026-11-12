[English](Step-4-International-Releases) · [Dansk](Step-4-International-Releases-da) · **Bahasa Malaysia**

# Langkah 4: Tapis pada berbilang syarat

**Soalan:** Filem manakah yang tidak memperoleh apa-apa di Amerika Syarikat tetapi memperoleh sesuatu di luar negara, dan filem manakah yang belum ditayangkan?

![Langkah 4: Tapis pada berbilang syarat](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-4-international-releases.png)

## Apa yang dilakukan kod

`international_releases` menggabungkan dua syarat dengan `.loc[]` dan `&` bitwise; setiap perbandingan memerlukan kurungnya sendiri kerana `&` lebih kuat mengikat daripada `==`. `international_releases_query` menulis tapisan yang sama sebagai rentetan untuk `.query()` dengan perkataan `and`. Kedua-duanya menemui **155** filem. `unreleased_films` menemui **7** filem yang ditayangkan selepas 1 Mei 2018, dan `remove_unreleased` memulangkan `data_clean` dengan **5,384** filem. **37.3 %** filem ini tidak memperoleh semula bajetnya (`share_losing_money`).

## Apa yang anda perolehi

- Menggabungkan syarat dengan `&` dan kurungan dalam `.loc[]`.
- Tapisan yang sama sebagai rentetan yang mudah dibaca dengan `.query('a == 0 and b != 0')`.
- Membuang baris dengan `.drop(index)` dan menyimpan salinan bersih untuk selebihnya analisis.

Sebelumnya: [Langkah 3: Filem tanpa hasil](Step-3-Zero-Revenue-ms) · Seterusnya: [Langkah 5: Carta gelembung Seaborn](Step-5-Bubble-Chart-ms)
