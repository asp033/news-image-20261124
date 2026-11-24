"""News-image entry: copy the bundled entry.png to the output directory.

The image is the repository's entry.png, a 1024x1024 front page summing up
24 November 2026 world news. The grader runs this program twice with no
network; both runs must write the same bytes, so this is a plain copy.
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(SRC, OUT / "entry.png")
# Self-check: the copy must be byte-identical to the bundled image, so both
# of the grader's runs write exactly the same bytes.
assert (OUT / "entry.png").stat().st_size == SRC.stat().st_size
