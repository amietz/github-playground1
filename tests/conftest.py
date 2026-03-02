"""Conftest – add the src layout to sys.path so tests find the package."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
