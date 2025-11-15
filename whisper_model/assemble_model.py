import pathlib
import sys

BASE = pathlib.Path(__file__).parent
CHUNKS_DIR = BASE / "chunks"
PART_PREFIX = "model.bin.part."

if not CHUNKS_DIR.exists():
    print("Chunks directory missing:", CHUNKS_DIR)
    sys.exit(1)

parts = sorted(
    p for p in CHUNKS_DIR.iterdir()
    if p.name.startswith(PART_PREFIX)
)
if not parts:
    print("No chunk files found. Expected files starting with", PART_PREFIX)
    sys.exit(1)

out_path = BASE / "model.bin"
print("Reassembling", len(parts), "parts ->", out_path)
with open(out_path, "wb") as out:
    for part in parts:
        print("Appending", part.name)
        with open(part, "rb") as src:
            out.write(src.read())

print("Done. Size:", out_path.stat().st_size, "bytes")
