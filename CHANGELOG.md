# Changelog

All notable changes to LEANN will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- SECURITY.md with comprehensive security policy and vulnerability reporting process
- CODE_OF_CONDUCT.md for community guidelines
- CHANGELOG.md to track version history

## [0.3.4] - 2025-01-11

### Current Features
- Graph-based selective recomputation with high-degree preserving pruning
- 97% storage savings compared to traditional vector databases
- Support for HNSW and DiskANN backends
- Multiple LLM providers (HuggingFace, Ollama, OpenAI-compatible APIs)
- MCP (Model Context Protocol) integration for live data sources
- AST-aware code chunking for Python, Java, C#, and TypeScript
- Metadata filtering with multiple operators
- Grep search for exact text matching
- CLI tool for document indexing and search
- RAG applications for:
  - Documents (PDF, TXT, MD, DOCX, PPTX)
  - Apple Mail
  - Browser history (Chrome)
  - WeChat chat history
  - ChatGPT conversations
  - Claude conversations
  - iMessage conversations
  - Slack messages (via MCP)
  - Twitter bookmarks (via MCP)
  - Code repositories
- Python 3.9-3.13 support
- Cross-platform: Ubuntu, Arch, WSL, macOS (ARM64/Intel)

## Version History Notes

For detailed release notes prior to 0.3.4, please see:
- [GitHub Releases](https://github.com/yichuan-w/LEANN/releases)
- [Release Guide](docs/RELEASE.md)

## Categories

Changes are grouped using the following categories:
- **Added** for new features
- **Changed** for changes in existing functionality
- **Deprecated** for soon-to-be removed features
- **Removed** for now removed features
- **Fixed** for any bug fixes
- **Security** for vulnerability fixes

## Contributing

Found a bug or want to request a feature? Please check our [Contributing Guide](docs/CONTRIBUTING.md).

---

[Unreleased]: https://github.com/yichuan-w/LEANN/compare/v0.3.4...HEAD
[0.3.4]: https://github.com/yichuan-w/LEANN/releases/tag/v0.3.4
