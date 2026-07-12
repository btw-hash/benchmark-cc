def compute_mean(values):
    """Public entry point. Validates input, returns the mean."""
    if not isinstance(values, list):
        raise TypeError("values must be a list")
    if len(values) == 0:
        raise ValueError("values must not be empty")
    return _sum_values(values) / len(values)
