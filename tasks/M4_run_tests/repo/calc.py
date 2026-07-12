def add(a, b):
    return a - b  # BUG: subtraction instead of addition


def multiply(a, b):
    result = 0
    for _ in range(b):
        result += a
    return result
