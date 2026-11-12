"""Integration test: the screenshot script writes the nine step images."""

import importlib.util
from pathlib import Path
from types import ModuleType

SCRIPT = Path(__file__).resolve().parents[2] / "scripts" / "make_screenshots.py"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
EXPECTED_NAMES = {
    "step-1-goals.png",
    "step-2-explore-and-clean.png",
    "step-3-zero-revenue.png",
    "step-4-international-releases.png",
    "step-5-bubble-chart.png",
    "step-6-decades.png",
    "step-7-regression-plots.png",
    "step-8-scikit-learn.png",
    "step-9-summary.png",
}


def _load_script() -> ModuleType:
    """Import scripts/make_screenshots.py by file path."""
    spec = importlib.util.spec_from_file_location("make_screenshots", SCRIPT)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_main_writes_nine_valid_png_files(tmp_path: Path) -> None:
    """Each expected image exists, is non-empty and has the PNG signature."""
    _load_script().main(tmp_path)

    files = sorted(tmp_path.glob("*.png"))
    assert {file.name for file in files} == EXPECTED_NAMES
    for file in files:
        assert file.read_bytes().startswith(PNG_SIGNATURE)
