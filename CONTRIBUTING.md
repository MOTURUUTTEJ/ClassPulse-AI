# Contributing to ClassPulse-AI

Thanks for your interest in improving ClassPulse-AI.

## Development Setup
1. Fork and clone the repository.
2. Create a virtual environment and activate it:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install backend dependencies used by your changes.
4. Run the backend locally:
   ```bash
   uvicorn ClassPulse_AI.backend.main:app --reload
   ```
5. Open `http://127.0.0.1:8000` and verify the UI loads.

## Code Style Guidelines
- Follow existing code style and structure in each file.
- Python: keep changes PEP 8 compatible and avoid unused imports.
- Frontend: use clear naming and keep logic readable in `ClassPulse_AI/ui/index.html`.
- Keep changes focused and avoid unrelated refactors.

## Testing Requirements
This repository currently has no automated test suite configured.
Before submitting a PR:
- Run a Python syntax check:
  ```bash
  python -m compileall ClassPulse_AI
  ```
- Manually verify key flows (transcription, AI insights, quiz generation).
- Include clear verification notes in your PR description.

## Pull Request Process
1. Create a branch from the latest `main`.
2. Keep PRs small and focused on one concern.
3. Update documentation when behavior or setup changes.
4. Ensure no secrets are committed.
5. Request review and address feedback promptly.
