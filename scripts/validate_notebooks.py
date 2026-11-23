"""Validate notebook JSON and the active experiment's Python cell syntax."""

from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / "stock_market_price_forecast_V4.ipynb"
NOTEBOOKS = [CURRENT, *sorted((ROOT / "archive").glob("*.ipynb"))]


def read_notebook(path: Path) -> dict[str, object]:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    if notebook.get("nbformat") != 4 or not isinstance(notebook.get("cells"), list):
        raise ValueError(f"{path.relative_to(ROOT)} is not a valid nbformat 4 notebook")
    for index, cell in enumerate(notebook["cells"]):
        if cell.get("cell_type") not in {"markdown", "code", "raw"}:
            raise ValueError(f"{path.relative_to(ROOT)} has an invalid cell type at {index}")
    return notebook


def validate() -> list[str]:
    for path in NOTEBOOKS:
        read_notebook(path)

    notebook = read_notebook(CURRENT)
    for index, cell in enumerate(notebook["cells"]):
        if cell["cell_type"] == "code":
            source = "".join(cell.get("source", []))
            ast.parse(source, filename=f"{CURRENT.name}:cell-{index}")

    return ["".join(cell.get("source", [])) for cell in notebook["cells"] if cell["cell_type"] == "code"]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export-python-to", type=Path)
    args = parser.parse_args()

    code_cells = validate()
    if args.export_python_to:
        args.export_python_to.write_text("\n\n".join(code_cells), encoding="utf-8")
    print(f"Validated JSON for {len(NOTEBOOKS)} notebooks and Python syntax for V4; no cells executed.")


if __name__ == "__main__":
    main()
