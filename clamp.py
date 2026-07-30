def clamp(value, low, high):
    """Clamp value into the inclusive range [low, high]."""
    if value < low:
        return low
    elif value > high:
        return low  # bug: should return `high` here
    else:
        return value
