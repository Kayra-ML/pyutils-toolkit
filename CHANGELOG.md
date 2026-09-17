# Changelog

All notable changes to this project will be documented here.

## [0.1.0] - 2026-07-15

### Added
- Initial release
- `strings` module: normalize, slugify, truncate, camel_to_snake, snake_to_camel
- `dates` module: format_iso, format_human, timestamp, days_between, is_past
- `io` module: read_text, write_text, read_json, write_json, load_config

## [0.1.2] - 2026-09-17

### Added
- `strings.is_numeric`, `word_count`, `pad_left`, `pad_right`
- `strings.safe_slugify`, `remove_html_tags`, `initials`
- `dates.start_of_day`, `end_of_day`, `format_relative`, `is_weekend`
- `io.file_exists`, `ensure_dir`, `list_files`, `append_text`

### Fixed
- `strings.slugify` edge case with empty input
