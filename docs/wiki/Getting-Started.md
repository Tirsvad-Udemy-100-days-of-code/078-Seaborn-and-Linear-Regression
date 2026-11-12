**English** · [Dansk](Getting-Started-da) · [Bahasa Malaysia](Getting-Started-ms)

# Getting started

Requirements: Python 3.13 or newer and Git. Runtime dependencies: `pandas`, `matplotlib`, `seaborn` and `scikit-learn`.

## Get the code

```bash
git clone https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/078-Seaborn-and-Linear-Regression.git
cd 078-Seaborn-and-Linear-Regression
```

## Windows (PowerShell)

Check that Python is 3.13 or newer, then create and use a local `.venv`:

```powershell
python --version
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell refuses to run `Activate.ps1`, allow scripts for your user once: `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`.

## Linux and macOS (bash)

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

On Debian and Ubuntu you may first need `sudo apt install python3-venv`.

## Run

The same commands work on every system once the `.venv` is active:

```bash
python -m movie_regression
python -m pytest
jupyter lab notebooks/Seaborn_and_Linear_Regression.ipynb
```

Leave the `.venv` with `deactivate`. Leave out `[dev]` in the install if you only want to run the analysis.

**What you gain:** a repeatable set-up (a virtual environment per project), a package you install in editable mode, and tests that prove each answer.

Previous: [Home](Home) · Next: [Step 1: The goals](Step-1-Goals)
