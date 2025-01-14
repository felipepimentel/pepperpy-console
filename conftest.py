"""Test configuration."""

from __future__ import annotations

import sys
from pathlib import Path

# Add mocks directory to Python path
MOCKS_DIR = Path(__file__).parent / "tests" / "mocks"
sys.path.insert(0, str(MOCKS_DIR))
