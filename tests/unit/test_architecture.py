import ast
from pathlib import Path

import pytest

SOURCE = Path(__file__).resolve().parents[2] / "src" / "movie_regression"
FORBIDDEN = {
    "domain": ("application", "infrastructure", "presentation"),
    "application": ("infrastructure", "presentation"),
    "infrastructure": ("presentation",),
}


def _imported_modules(path: Path) -> list[str]:
    modules: list[str] = []
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            modules.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            modules.append(node.module)
    return modules


@pytest.mark.parametrize("layer", sorted(FORBIDDEN))
def test_inner_layer_imports_no_outer_layer(layer: str) -> None:
    offenders = [
        f"{path.name} imports {module}"
        for path in (SOURCE / layer).glob("*.py")
        for module in _imported_modules(path)
        for outer in FORBIDDEN[layer]
        if module.startswith(f"movie_regression.{outer}")
    ]

    assert offenders == []
