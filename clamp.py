def clamp(value, low, high):
    """Clamp value into the inclusive range [low, high]."""
    if low > high:
        raise ValueError("low must be <= high")
    if value < low:
        return low
    elif value > high:
        return high
    else:
        return value
