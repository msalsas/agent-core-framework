#!/usr/bin/env bash
# Simple release script: builds and uploads to PyPI using TWINE_PASSWORD
# Usage: TWINE_PASSWORD=your_token ./scripts/release.sh
set -euo pipefail

python -m pip install --upgrade build twine
python -m build
python -m twine upload dist/*

echo "Published distributions in dist/ to PyPI (twine)."
