# pyutils-toolkit

A lightweight Python utility library for common data processing tasks.

## Features

- String manipulation helpers
- Date/time formatting utilities
- File I/O wrappers
- Simple logging configuration
- Config parser with env override support

## Installation

```bash
pip install pyutils-toolkit
```

## Usage

```python
from pyutils import strings, dates, io

# Clean and normalize a string
cleaned = strings.normalize("  Hello   World  ")

# Format a date
formatted = dates.format_iso(datetime.now())

# Read config with env override
config = io.load_config("config.yaml")
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first.

## License

MIT

## More Examples

```python
from pyutils import strings, dates

# Slugify a title
slug = strings.slugify("Hello World! This is a Test")
# -> "hello-world-this-is-a-test"

# Word count
count = strings.word_count("The quick brown fox")
# -> 4
```


## More Examples

```python
from pyutils import strings, dates

# Slugify a title
slug = strings.slugify("Hello World! This is a Test")
# -> "hello-world-this-is-a-test"

# Word count
count = strings.word_count("The quick brown fox")
# -> 4
```
