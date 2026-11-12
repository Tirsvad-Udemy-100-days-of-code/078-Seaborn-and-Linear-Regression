"""Integration test: the course notebook runs from top to bottom."""

import shutil
from pathlib import Path

import pytest

NOTEBOOK = (
    Path(__file__).resolve().parents[2]
    / "notebooks"
    / "Seaborn_and_Linear_Regression.ipynb"
)
TIMEOUT_SECONDS = 300
STEP_COUNT = 9


def test_notebook_executes_and_has_nine_step_headings(tmp_path: Path) -> None:
    """Run a copy of the notebook from another folder; the repo file is kept."""
    nbformat = pytest.importorskip("nbformat", reason="nbformat is not installed")
    nbclient = pytest.importorskip("nbclient", reason="nbclient is not installed")
    pytest.importorskip("ipykernel", reason="ipykernel is not installed")
    copy = tmp_path / NOTEBOOK.name
    shutil.copyfile(NOTEBOOK, copy)

    notebook = nbformat.read(copy, as_version=4)
    nbclient.NotebookClient(
        notebook,
        timeout=TIMEOUT_SECONDS,
        kernel_name="python3",
        resources={"metadata": {"path": str(tmp_path)}},
    ).execute()

    markdown = "\n".join(
        cell.source for cell in notebook.cells if cell.cell_type == "markdown"
    )
    for number in range(1, STEP_COUNT + 1):
        assert f"## Step {number}:" in markdown
