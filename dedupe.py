def dedupe_preserve_order(items):
    """Return a new list with duplicates removed, keeping the first
    occurrence of each item and preserving the original order."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result
