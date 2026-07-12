def moving_average(values, window):
    """Return a list of moving averages of `values` over `window` items.

    For input of length N and window W, output has length N - W + 1.
    Each output[i] is the average of values[i : i + W].
    """
    if window <= 0:
        raise ValueError("window must be positive")
    if window > len(values):
        return []
    result = []
    for i in range(len(values) - window):
        chunk = values[i : i + window]
        result.append(sum(chunk) / window)
    return result
