# Contributing to ClassPulse AI

Thank you for your interest in contributing.

## Development Setup

1. Fork this repository and clone your fork.
2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
3. Install backend dependencies used by your feature/fix.
4. Copy `.env.example` to `.env` and fill in your own values.

## Run the Project Locally

From the repository root:

```bash
uvicorn ClassPulse_AI.backend.main:app --reload
```

Open `http://127.0.0.1:8000` in your browser.

## Testing

There is currently no dedicated automated test suite in this repository.
Before submitting, run at least:

```bash
python -m compileall ClassPulse_AI/backend/main.py
```

Also manually verify key flows in the UI (transcription, AI insights, and quiz generation).

## Code Style

- Follow existing code formatting and naming conventions.
- Keep changes small and focused.
- Avoid introducing hardcoded secrets or credentials.
- Update documentation when behavior/setup changes.

## Pull Request Process

1. Create a feature branch from `main`.
2. Make focused commits with clear commit messages.
3. Ensure local checks pass and docs are updated if needed.
4. Open a pull request describing:
   - What changed
   - Why it changed
   - How it was tested
5. Address review feedback and keep the PR scope minimal.
