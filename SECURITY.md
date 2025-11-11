# Security Policy

## Supported Versions

We release patches for security vulnerabilities for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.3.x   | :white_check_mark: |
| < 0.3.0 | :x:                |

## Reporting a Vulnerability

The LEANN team takes security seriously. We appreciate your efforts to responsibly disclose your findings.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report security vulnerabilities by:

1. **Email**: Send an email to the maintainers (see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for contact information)
2. **GitHub Security Advisory**: Use GitHub's [Private Vulnerability Reporting](https://github.com/yichuan-w/LEANN/security/advisories/new)

Please include the following information:

- Type of vulnerability
- Full paths of source file(s) related to the manifestation of the vulnerability
- Location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

### Response Timeline

- **Acknowledgment**: We will acknowledge receipt of your vulnerability report within 48 hours
- **Assessment**: We will assess the vulnerability and determine its severity within 5 business days
- **Updates**: We will provide regular updates on our progress every 7 days
- **Resolution**: We aim to release a fix within 30 days for high-severity issues

### What to Expect

After you submit a report:

1. We will confirm receipt and begin investigating the issue
2. We will keep you informed about our progress
3. We will work with you to understand the issue and develop a fix
4. Once a fix is ready, we will notify you before public disclosure
5. We will publicly disclose the vulnerability after a fix is released
6. We will credit you in the release notes (unless you prefer to remain anonymous)

## Security Best Practices

When using LEANN, we recommend:

### For Users

1. **Keep LEANN Updated**: Always use the latest stable version
2. **Validate Input**: Sanitize and validate all user inputs before indexing
3. **Secure API Keys**: Never commit API keys (OpenAI, Ollama, etc.) to version control
   - Use environment variables: `OPENAI_API_KEY`, `SLACK_BOT_TOKEN`, etc.
   - Use `.env` files (listed in `.gitignore`)
4. **File Permissions**: Ensure index files have appropriate permissions
5. **Network Security**: When using embedding servers, ensure proper network isolation
6. **Data Privacy**: Be cautious when indexing sensitive data:
   - LEANN runs locally by default (privacy-preserving)
   - Review cloud provider privacy policies before using cloud embedding APIs

### For Developers

1. **Dependency Security**: Regularly update dependencies
2. **Input Validation**: Validate all inputs in public APIs
3. **Error Handling**: Avoid exposing sensitive information in error messages
4. **Code Review**: Security-focused code reviews for all changes
5. **Static Analysis**: Run linters and security scanners:
   ```bash
   uv run --only-group lint pre-commit run --all-files
   ```

## Known Security Considerations

### Embedding Providers

- **Local Models (Recommended)**: Using Ollama or HuggingFace models ensures complete data privacy
- **Cloud APIs**: When using OpenAI or other cloud APIs, your data is sent to third-party servers
  - Review their privacy and data retention policies
  - Be aware of potential data usage for model training
  - Consider data sensitivity before using cloud providers

### MCP Integration

- **Authentication**: MCP servers (Slack, Twitter, etc.) require API credentials
  - Store credentials securely using environment variables
  - Never commit credentials to version control
  - Rotate credentials regularly

### Index Files

- **File Access**: Index files (`.leann` directories) contain embeddings and metadata
  - Protect with appropriate file system permissions
  - Be cautious when sharing index files (they may contain sensitive content)

## Security Updates

Security updates will be announced through:

- GitHub Security Advisories
- Release notes in [CHANGELOG.md](CHANGELOG.md)
- GitHub Releases page

## Attribution

We will acknowledge security researchers who report valid vulnerabilities in our release notes and security advisories (unless anonymity is requested).

## Questions?

For questions about this security policy, please open an issue on GitHub or contact the maintainers through the channels listed in [CONTRIBUTING.md](docs/CONTRIBUTING.md).

---

**Note**: This security policy is inspired by industry best practices and adapted for the LEANN project's specific needs.
