# Changelog

All notable changes to DecisionMap should be recorded here.

The format is intentionally lightweight and follows human-readable release notes rather than strict automation metadata.

## [v0.3.0] - 2026-09-11

### Added

- self-contained `decision-map` Agent Skill with Codex metadata
- validation for user-supplied strategy-map and cascade-log JSON files
- repository-wide release checks, security policy, and dependency updates

### Changed

- quick start now leads with one-command skill installation
- JSON validation auto-discovers bundled fixtures and enforces date formats
- CI actions and contributor documentation are current for the v0.3 release
- ABVX integrations are presented as optional companions rather than required dependencies

## [v0.2.0] - 2026-06-06

### Added

- canonical agri/commodities strategy-map example
- canonical FMCG route-to-market full-run example
- cascade-log markdown template and worked example
- machine-readable JSON fixtures for strategy map and cascade log
- public example validation script and CI workflow
- `CONTRIBUTING.md` and issue templates

### Changed

- `README.md` is now the primary entrypoint
- `USAGE.md` is now a narrower operator runbook
- `protocol.md` is now a tighter normative spec
- Stage 6 cascade log is now treated as a first-class capability

### Notes

- Schema shape remains stable in this release line; examples and docs now enforce it more clearly.
