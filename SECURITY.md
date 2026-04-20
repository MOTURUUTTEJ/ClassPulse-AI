# Security Policy

## API Key Security Best Practices
- Never hardcode API keys in tracked source files.
- Use environment variables for backend integrations.
- Scope API keys to the minimum required permissions.
- Rotate API keys immediately if exposure is suspected.
- Use separate keys for development and production.

## Environment Variable Handling
- Store local secrets in a non-tracked `.env` file.
- Keep a `.env.example` template with placeholder values only.
- Validate required environment variables at startup.
- Do not print secret values in logs, errors, or screenshots.

## Credential Management
- Use a password manager or secret manager for credential storage.
- Grant access to credentials only to contributors who need it.
- Revoke credentials when collaborators leave the project.
- Avoid sharing credentials over chat, email, or issue threads.

## Never Commit Secrets
Committing secrets is a critical risk. Before pushing:
- Review `git diff` for accidental key/token exposure.
- Check staged files for `.env`, private keys, and credentials.
- Regenerate and revoke any exposed secret immediately.

## Responsible Disclosure
If you discover a vulnerability:
1. Do **not** open a public issue with exploit details.
2. Report it privately to the maintainer with reproduction steps and impact.
3. Allow reasonable time for triage and remediation before disclosure.

Maintainer contact for security reports: open a private communication channel with the repository owner on GitHub and include `[SECURITY]` in the subject/title.
