# Security Policy

## Reporting a Vulnerability

If you discover a security issue, please open a private/security report through GitHub Security Advisories (preferred) or contact the maintainer directly with reproduction details.

## API Keys and Secrets

- Never hardcode API keys in source files.
- Never commit real secrets to Git.
- Use environment variables through a local `.env` file.

## Environment Variable Setup

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Replace placeholders with your own values.
3. Keep `.env` local only (`.gitignore` is configured to exclude it).

## Security Best Practices for This Project

- Rotate keys immediately if a secret is exposed.
- Use separate credentials for development and production.
- Limit key permissions/scopes where possible.
- Review PRs for accidental secret exposure before merge.
- Remove generated artifacts or logs if they may contain sensitive data.
