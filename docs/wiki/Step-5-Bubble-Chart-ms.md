[English](Step-5-Bubble-Chart) · [Dansk](Step-5-Bubble-Chart-da) · **Bahasa Malaysia**

# Langkah 5: Carta gelembung Seaborn

**Soalan:** Bagaimanakah bajet dan hasil berkaitan, dan bagaimana industri filem telah berubah?

![Langkah 5: Carta gelembung Seaborn](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn_and_Linear_Regression/raw/branch/main/docs/images/step-5-bubble-chart.png)

## Apa yang dilakukan kod

`bubble_chart` memanggil `sns.scatterplot` dengan bajet pada paksi x dan hasil seluruh dunia pada paksi y. Apabila `hue` dan `size` diberi hasil seluruh dunia, plot serakan menjadi **carta gelembung** dengan dimensi ketiga. Gaya `darkgrid`, had paksi dan label "Budget in $100 millions" dan "Revenue in $ billions" ditetapkan pada paksi Matplotlib. `bubble_chart_by_date` meletakkan tarikh tayangan pada paksi x untuk menunjukkan bagaimana bajet melonjak sepanjang dekad.

## Apa yang anda perolehi

- Seaborn dibina di atas Matplotlib: anda sentiasa boleh turun ke lapisan Matplotlib dengan `ax.set(...)`.
- `sns.scatterplot(hue=..., size=...)` menambah dimensi ketiga dan keempat pada carta.
- `with sns.axes_style('darkgrid'):` menggayakan carta tanpa menukar gaya global.

Sebelumnya: [Langkah 4: Tapis pada berbilang syarat](Step-4-International-Releases-ms) · Seterusnya: [Langkah 6: Pembahagian lantai untuk menukar tahun kepada dekad](Step-6-Decades-ms)
