# Faster Whisper Small (Chunked Model)

This folder will contain the chunked parts of `model.bin` once the GitHub Action runs.

Reassemble after cloning:

```bash
python whisper_model/assemble_model.py
```

Result: `whisper_model/model.bin`

Then point faster-whisper to `whisper_model` as the model directory.

Chunks are created by the workflow `.github/workflows/chunk_and_commit.yml`.
