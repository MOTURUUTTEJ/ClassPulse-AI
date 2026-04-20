# Contributing to ClassPulse-AI

Thanks for your interest in contributing! This guide keeps contributions consistent, secure, and easy to review.

## Development setup

1. Fork and clone the repository.
2. Create a branch from `main`:
   ```bash
   git checkout -b feat/short-description
   ```
3. Start the project:
   - **Frontend only:** open `ClassPulse_AI/ui/index.html` in Chrome/Edge.
   - **Backend (optional):** run FastAPI from `ClassPulse_AI/backend/main.py` if you are working on backend routes.
4. For local experimentation, use your own API credentials and never commit them.

## Code style guidelines

- Keep changes small and focused.
- Prefer clear, readable names.
- Reuse existing patterns in `main.py` and `index.html`.
- Do not commit generated artifacts, secrets, or local environment files.
- Update documentation (`README.md`, `SECURITY.md`) when behavior changes.

## Pull request process

1. Keep PRs scoped to one problem.
2. Include:
   - What changed
   - Why it changed
   - How it was verified
3. Reference related issue(s) when possible.
4. Ensure no secrets are included in the diff.
5. Wait for review before merging.

## Issue reporting guidelines

When opening an issue, include:

- Clear title and summary
- Steps to reproduce
- Expected vs actual behavior
- Browser/OS details (for UI issues)
- Logs or screenshots when relevant

For security-sensitive issues, **do not file a public issue**. Follow `SECURITY.md` instead.
