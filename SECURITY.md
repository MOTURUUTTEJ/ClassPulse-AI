# Security Policy

## Supported versions

This project is actively maintained on the default branch. Security fixes are prioritized there.

## Reporting a vulnerability

Please report vulnerabilities responsibly:

- Do **not** open public GitHub issues for security vulnerabilities.
- Email the maintainer directly with:
  - Affected component
  - Reproduction steps / proof of concept
  - Impact assessment
  - Suggested remediation (optional)

The maintainer will acknowledge receipt and work on validation and remediation as quickly as possible.

## Secret and API key handling

- Never commit API keys, tokens, or `.env` files.
- Use environment variables or local-only configuration for secrets.
- Rotate exposed keys immediately.
- Use least privilege and provider-side restrictions (allowed origins, quotas, etc.).
