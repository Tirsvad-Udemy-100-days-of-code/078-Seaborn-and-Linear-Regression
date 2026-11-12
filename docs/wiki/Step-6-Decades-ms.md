[English](Step-6-Decades) · [Dansk](Step-6-Decades-da) · **Bahasa Malaysia**

# Langkah 6: Pembahagian lantai untuk menukar tahun kepada dekad

**Soalan:** Bagaimanakah kita mengumpulkan filem mengikut dekad?

![Langkah 6: Pembahagian lantai untuk menukar tahun kepada dekad](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn_and_Linear_Regression/raw/branch/main/docs/images/step-6-decades.png)

## Apa yang dilakukan kod

`add_decade` membuat `DatetimeIndex` daripada `Release_Date`, mengambil `.year` dan menggunakan pembahagian lantai: `year // 10 * 10`, jadi 1992 dan 1999 kedua-duanya menjadi **1990**. Peraturan itu hanya wujud di satu tempat, iaitu `to_decade` dalam lapisan domain. `split_old_and_new` kemudian memisahkan **153** filem lama (sebelum 1970) daripada **5,231** filem baharu, dan `decade_chart` mengira filem bagi setiap dekad: industri berkembang pesat selepas 1970.

## Apa yang anda perolehi

- `//` (pembahagian lantai) membuang bakinya: `1999 // 10 * 10 == 1990`.
- `pd.DatetimeIndex(lajur).year` mengeluarkan tahun daripada tarikh.
- Menambah lajur terterbit untuk mengumpul, mengira dan memisahkan DataFrame.

Sebelumnya: [Langkah 5: Carta gelembung Seaborn](Step-5-Bubble-Chart-ms) · Seterusnya: [Langkah 7: Plot regresi dengan Seaborn](Step-7-Regression-Plots-ms)
