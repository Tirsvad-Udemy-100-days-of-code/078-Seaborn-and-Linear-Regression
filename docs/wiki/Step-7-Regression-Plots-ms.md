[English](Step-7-Regression-Plots) · [Dansk](Step-7-Regression-Plots-da) · **Bahasa Malaysia**

# Langkah 7: Plot regresi dengan Seaborn

**Soalan:** Adakah garis lurus menerangkan bagaimana bajet membawa kepada hasil?

![Langkah 7: Plot regresi dengan Seaborn](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn_and_Linear_Regression/raw/branch/main/docs/images/step-7-regression-plots.png)

## Apa yang dilakukan kod

`regression_chart` memanggil `sns.regplot`, yang melukis plot serakan, garis regresi linear dan selang keyakinannya dalam satu panggilan. Bagi **filem lama** titik-titiknya jauh daripada garis: bajet tidak banyak menerangkan hasil. Bagi **filem baharu** titik-titik mengikut garis dengan jauh lebih baik. Gaya ditetapkan melalui `scatter_kws` (contohnya `alpha`) dan `line_kws` (contohnya warna); carta filem baharu menggunakan titik biru tua (`#2f4b7c`), garis oren (`#ff7c43`), `darkgrid` dan paksi yang tidak menunjukkan nilai negatif.

## Apa yang anda perolehi

- `sns.regplot` menunjukkan data dan garis regresi bersama-sama.
- `scatter_kws` dan `line_kws` menerima kamus untuk titik dan garis.
- Menilai regresi dengan mata: sejauh manakah titik-titik daripada garis?

Sebelumnya: [Langkah 6: Pembahagian lantai untuk menukar tahun kepada dekad](Step-6-Decades-ms) · Seterusnya: [Langkah 8: Jalankan regresi anda sendiri dengan scikit-learn](Step-8-Scikit-Learn-ms)
