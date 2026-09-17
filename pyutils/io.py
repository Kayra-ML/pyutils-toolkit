"""
File I/O wrappers and config loader.
"""
import os
import json
from pathlib import Path
from typing import Any, Optional


def read_text(path: str, encoding: str = "utf-8") -> str:
    """Read a text file and return its contents."""
    return Path(path).read_text(encoding=encoding)


def write_text(path: str, content: str, encoding: str = "utf-8") -> None:
    """Write content to a text file, creating parent dirs if needed."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding=encoding)


def read_json(path: str) -> Any:
    """Read and parse a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, data: Any, indent: int = 2) -> None:
    """Serialize data to a JSON file."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=indent, ensure_ascii=False)


def load_config(path: str, env_prefix: Optional[str] = None) -> dict:
    """
    Load a JSON config file.
    If env_prefix is set, override keys with matching env vars.
    e.g. env_prefix='APP' overrides 'debug' with APP_DEBUG env var.
    """
    config = read_json(path)
    if env_prefix:
        for key in list(config.keys()):
            env_key = f"{env_prefix}_{key.upper()}"
            if env_key in os.environ:
                config[key] = os.environ[env_key]
    return config

def file_exists(path: str) -> bool:
    """Return True if path exists and is a file."""
    return Path(path).is_file()


def ensure_dir(path: str):
    """Create directory (and parents) if it doesn't exist. Returns Path."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def list_files(directory: str, extension=None) -> list:
    """List files in a directory, optionally filtered by extension."""
    p = Path(directory)
    if extension:
        return sorted(p.glob(f"*.{extension.lstrip('.')}"))
    return sorted(f for f in p.iterdir() if f.is_file())


def append_text(path: str, content: str, encoding: str = "utf-8") -> None:
    """Append content to a text file, creating it if it doesn't exist."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a", encoding=encoding) as f:
        f.write(content)
