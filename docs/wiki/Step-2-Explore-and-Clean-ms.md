[English](Step-2-Explore-and-Clean) · [Dansk](Step-2-Explore-and-Clean-da) · **Bahasa Malaysia**

# Langkah 2: Teroka dan bersihkan data

**Soalan:** Bagaimanakah data distrukturkan, dan bagaimana kita menjadikan lajur wang berangka?

![Langkah 2: Teroka dan bersihkan data](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression/raw/branch/main/docs/images/step-2-explore-and-clean.png)

## Apa yang dilakukan kod

`describe_structure` mendapati **5,391 baris dan 6 lajur, tiada nilai NaN dan tiada pendua**. `convert_money_to_numbers` membuang `$` dan `,` dengan gelung bersarang ke atas tiga lajur wang, dan `convert_release_date` menjadikan `Release_Date` sebagai datetime. `summary_statistics` (`.describe()`) menunjukkan purata bajet kira-kira **$31 juta** dan purata hasil seluruh dunia kira-kira **$89 juta**; bajet tertinggi ialah $425,000,000 dan hasil seluruh dunia tertinggi ialah $2,783,918,982. Filem termurah, *My Date With Drew*, berharga $1,100 dan memperoleh $181,041.

## Apa yang anda perolehi

- `.shape`, `.head()`, `.info()`, `.isna()` dan `.duplicated()` sebagai semakan pertama yang standard.
- Membersihkan teks dengan `.str.replace()` dalam gelung bersarang, kemudian `pd.to_numeric`.
- `pd.to_datetime` untuk tarikh, dan `.describe()` untuk gambaran pantas tentang angka.

Sebelumnya: [Langkah 1: Matlamat](Step-1-Goals-ms) · Seterusnya: [Langkah 3: Filem tanpa hasil](Step-3-Zero-Revenue-ms)
