"""
Date and time formatting utilities.
"""
from datetime import datetime, timezone
from typing import Optional


def format_iso(dt: Optional[datetime] = None) -> str:
    """Return ISO 8601 formatted datetime string."""
    if dt is None:
        dt = datetime.now(timezone.utc)
    return dt.isoformat()


def format_human(dt: Optional[datetime] = None) -> str:
    """Return human-readable datetime string."""
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%B %d, %Y at %H:%M")


def timestamp() -> int:
    """Return current UTC Unix timestamp."""
    return int(datetime.now(timezone.utc).timestamp())


def days_between(start: datetime, end: datetime) -> int:
    """Return number of days between two datetimes."""
    return abs((end - start).days)


def is_past(dt: datetime) -> bool:
    """Check if a datetime is in the past."""
    return dt < datetime.now(dt.tzinfo)