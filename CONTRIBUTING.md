# Contributing to ClassPulse AI

Thank you for contributing to ClassPulse AI.

## Development Setup
1. Fork and clone the repository.
2. Create a feature branch from `main`.
3. If you are working on the backend, create and activate a Python virtual environment.
4. Install backend dependencies used by your change.
5. Run the app locally:
   - Frontend: open `ClassPulse_AI/ui/index.html` in a supported browser.
   - Backend (optional): run `uvicorn ClassPulse_AI.backend.main:app --reload`.

## Code Standards and Conventions
- Keep changes small and focused.
- Follow existing naming and formatting conventions in each file.
- Prefer clear, readable logic over clever one-liners.
- Never hardcode secrets, API keys, or credentials in code.

## Issues and Pull Requests
- Use issues for bugs, feature requests, and discussion.
- For PRs, include:
  - What changed
  - Why it changed
  - How to test it
  - Screenshots/GIFs for UI updates when applicable
- Link related issues in your PR description.

## Testing Requirements
- Run all existing tests/checks related to your changes.
- For UI-only changes, manually test the affected flows in browser.
- Ensure no secrets are introduced in committed files.

## Commit Message Guidelines
Use clear, imperative commit messages.
- Preferred format: `type(scope): short summary`
- Examples:
  - `docs(readme): add environment setup and troubleshooting`
  - `fix(ui): handle empty transcript before analysis`
  - `chore(gitignore): add node and env patterns`
