def parse_config(text: str) -> dict:
    """Parse a key=value config string into a dictionary.

    Rules:
    - Lines starting with '#' are comments (skip them)
    - Empty lines are skipped
    - Keys and values are stripped of whitespace
    - Values may contain '=' characters (e.g., URLs)
    - Section headers like [database] group keys: "host" becomes "database.host"
    - Keys before any section header have no prefix
    - Duplicate keys: last value wins
    """
    result = {}
    current_section = None
    for line in text.strip().split('\n'):
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        if line.startswith('[') and line.endswith(']'):
            current_section = line[1:-1]
            continue
        if '=' not in line:
            continue
        key, value = line.split('=', 1)
        key = key.strip()
        value = value.strip()
        # TODO: if inside a section, prefix the key with the section name and a dot
        result[key] = value
    return result



def truncate(text: str, max_length: int) -> str:
    """Truncate text to the given maximum length.

    If the text is longer than max_length, truncate it and append "..."
    so the total length of the returned string is max_length + 3.
    If the text is already within max_length, return it unchanged.

    Args:
        text: The input string.
        max_length: The maximum number of characters before truncation.

    Returns:
        The original text if short enough, or the truncated text with "..." appended.
    """
    pass  # TODO: implement this function
