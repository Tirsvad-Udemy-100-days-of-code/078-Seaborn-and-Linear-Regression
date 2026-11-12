[English](Getting-Started) · **Dansk** · [Bahasa Malaysia](Getting-Started-ms)

# Kom godt i gang

Krav: Python 3.13 eller nyere og Git. Afhængigheder ved kørsel: `pandas`, `matplotlib`, `seaborn` og `scikit-learn`.

## Hent koden

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn_and_Linear_Regression.git
cd 078-Seaborn_and_Linear_Regression
```

## Windows (PowerShell)

Kontrollér, at Python er 3.13 eller nyere, og opret og brug derefter et lokalt `.venv`:

```powershell
python --version
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

Hvis PowerShell nægter at køre `Activate.ps1`, så tillad scripts for din bruger én gang: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## Linux og macOS (bash)

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

På Debian og Ubuntu skal du måske først køre `sudo apt install python3-venv`.

## Kør

De samme kommandoer virker på alle systemer, når `.venv` er aktivt:

```bash
python -m movie_regression
python -m pytest
jupyter lab notebooks/Seaborn_and_Linear_Regression.ipynb
```

Forlad `.venv` med `deactivate`. Udelad `[dev]` ved installationen, hvis du kun vil køre analysen.

**Hvad du får ud af det:** en gentagelig opsætning (et virtuelt miljø pr. projekt), en pakke, du installerer i redigerbar tilstand, og tests, der beviser hvert svar.

Forrige: [Hjem](Home-da) · Næste: [Trin 1: Målene](Step-1-Goals-da)
