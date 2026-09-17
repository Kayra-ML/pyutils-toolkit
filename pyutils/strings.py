"""
String manipulation helpers.
"""
import re
import unicodedata


def normalize(s: str) -> str:
    """Strip and collapse whitespace."""
    return re.sub(r'\s+', ' ', s.strip())


def slugify(s: str) -> str:
    """Convert string to URL-friendly slug."""
    s = unicodedata.normalize('NFKD', s)
    s = s.encode('ascii', 'ignore').decode('ascii')
    s = re.sub(r'[^\w\s-]', '', s).strip().lower()
    return re.sub(r'[-\s]+', '-', s)


def truncate(s: str, max_len: int = 100, suffix: str = '...') -> str:
    """Truncate string to max_len characters."""
    if len(s) <= max_len:
        return s
    return s[:max_len - len(suffix)] + suffix


def camel_to_snake(name: str) -> str:
    """Convert camelCase to snake_case."""
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def snake_to_camel(name: str) -> str:
    """Convert snake_case to camelCase."""
    components = name.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def is_numeric(s: str) -> bool:
    """Return True if string represents a numeric value."""
    try:
        float(s)
        return True
    except ValueError:
        return False


def pad_left(s: str, width: int, char: str = ' ') -> str:
    """Left-pad string to given width."""
    return s.rjust(width, char)


def pad_right(s: str, width: int, char: str = ' ') -> str:
    """Right-pad string to given width."""
    return s.ljust(width, char)


def word_count(s: str) -> int:
    """Return the number of words in a string."""
    return len(s.split())


def safe_slugify(s: str, fallback: str = "untitled") -> str:
    """Slugify with a fallback for empty or whitespace-only strings."""
    result = slugify(s)
    return result if result else fallback


def pad_left(s: str, width: int, char: str = ' ') -> str:
    """Left-pad string to given width."""
    return s.rjust(width, char)


def pad_right(s: str, width: int, char: str = ' ') -> str:
    """Right-pad string to given width."""
    return s.ljust(width, char)


def remove_html_tags(s: str) -> str:
    """Strip HTML tags from a string."""
    return re.sub(r'<[^>]+>', '', s)
