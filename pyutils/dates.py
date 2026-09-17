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

def start_of_day(dt: Optional[datetime] = None) -> datetime:
    """Return midnight (start) of the given date."""
    if dt is None:
        dt = datetime.now()
    return dt.replace(hour=0, minute=0, second=0, microsecond=0)


def end_of_day(dt=None):
    """Return 23:59:59 (end) of the given date."""
    from datetime import datetime
    if dt is None:
        dt = datetime.now()
    return dt.replace(hour=23, minute=59, second=59, microsecond=999999)


def format_relative(dt) -> str:
    """Return a human-readable relative time string (e.g. '3 days ago')."""
    from datetime import datetime
    now = datetime.now(dt.tzinfo)
    diff = now - dt
    days = diff.days
    if days == 0:
        secs = diff.seconds
        if secs < 60:
            return "just now"
        elif secs < 3600:
            return f"{secs // 60} minutes ago"
        else:
            return f"{secs // 3600} hours ago"
    elif days == 1:
        return "yesterday"
    elif days < 30:
        return f"{days} days ago"
    else:
        return f"{days // 30} months ago"


def is_weekend(dt=None) -> bool:
    """Return True if the given date falls on a Saturday or Sunday."""
    from datetime import datetime
    if dt is None:
        dt = datetime.now()
    return dt.weekday() >= 5
