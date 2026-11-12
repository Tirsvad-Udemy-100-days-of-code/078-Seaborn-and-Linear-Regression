[English](Getting-Started) · [Dansk](Getting-Started-da) · **Bahasa Malaysia**

# Bermula

Keperluan: Python 3.13 atau lebih baharu dan Git. Kebergantungan masa jalan: `pandas`, `matplotlib`, `seaborn` dan `scikit-learn`.

## Dapatkan kod

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn_and_Linear_Regression.git
cd 078-Seaborn_and_Linear_Regression
```

## Windows (PowerShell)

Semak bahawa Python ialah 3.13 atau lebih baharu, kemudian cipta dan gunakan `.venv` tempatan:

```powershell
python --version
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Jika PowerShell enggan menjalankan `Activate.ps1`, benarkan skrip untuk pengguna anda sekali sahaja: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## Linux dan macOS (bash)

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Pada Debian dan Ubuntu anda mungkin perlu menjalankan `sudo apt install python3-venv` dahulu.

## Jalankan

Arahan yang sama berfungsi pada semua sistem apabila `.venv` aktif:

```bash
python -m movie_regression
python -m pytest
jupyter lab notebooks/Seaborn_and_Linear_Regression.ipynb
```

Keluar daripada `.venv` dengan `deactivate`. Tinggalkan `[dev]` semasa pemasangan jika anda hanya mahu menjalankan analisis.

**Apa yang anda perolehi:** persediaan yang boleh diulang (satu persekitaran maya bagi setiap projek), pakej yang dipasang dalam mod boleh sunting, dan ujian yang membuktikan setiap jawapan.

Sebelumnya: [Utama](Home-ms) · Seterusnya: [Langkah 1: Matlamat](Step-1-Goals-ms)
