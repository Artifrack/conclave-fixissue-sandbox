def flatten_one_level(list_of_lists):
    """Flatten a list of lists by exactly one level."""
    result = []
    for sublist in list_of_lists:
        result.extend(sublist)
    return result
