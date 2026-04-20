# Security Policy

## Supported Versions
This project is actively maintained on the `main` branch.

## API Key and Credential Safety
- Never hardcode API keys, tokens, or passwords in committed source files.
- Never commit `.env` files or any file containing credentials.
- Rotate exposed keys immediately if you suspect leakage.
- Use least-privilege API keys scoped only to required services.
- Use separate keys for development, staging, and production.

## Safe Credential Handling
- For local development, store secrets in environment variables or a local untracked `.env` file.
- For production deployments, use your hosting provider's secret manager.
- Avoid logging secret values in terminal output, server logs, or browser console.
- Review pull requests for accidental key exposure before merging.

## Security Considerations
- Validate and sanitize all user-provided input before using it in prompts or downstream APIs.
- Keep dependencies up to date and patch known vulnerabilities quickly.
- Restrict CORS and network exposure when deploying the backend publicly.
- Ensure HTTPS is used in production to protect traffic in transit.

## Reporting a Vulnerability
If you discover a security issue:
1. **Do not** create a public issue with exploit details.
2. Use GitHub private vulnerability reporting (Security Advisories) for this repository.
3. If private reporting is unavailable, open a minimal issue asking maintainers for a secure contact channel.

Please include reproduction steps, impact, and suggested mitigations where possible.
