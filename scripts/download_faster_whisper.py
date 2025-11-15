import os
import requests
import pathlib

BASE = "https://huggingface.co/guillaumekln/faster-whisper-small/resolve/main"
FILES = ["config.json", "model.bin", "tokenizer.json", "vocabulary.txt"]
TOKEN = os.getenv("HF_TOKEN")
if not TOKEN:
    raise SystemExit("HF_TOKEN missing (set GitHub secret HF_TOKEN)")

headers = {"Authorization": f"Bearer {TOKEN}"}
out_dir = pathlib.Path("model_tmp")
out_dir.mkdir(exist_ok=True)

for fname in FILES:
    url = f"{BASE}/{fname}"
    print(f"Downloading {fname} ...")
    r = requests.get(url, headers=headers, stream=True, timeout=60)
    r.raise_for_status()
    size = 0
    with open(out_dir / fname, "wb") as fh:
        for chunk in r.iter_content(1024 * 1024):
            if chunk:
                fh.write(chunk)
                size += len(chunk)
    print(f"Done {fname}: {size} bytes")

print("All files downloaded to", out_dir)
