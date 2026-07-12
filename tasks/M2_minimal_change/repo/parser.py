def parse_version(s):
    parts = s.split(".")
    return tuple(int(p) for p in parts)


def compare_versions(a, b):
    """Return -1 if a < b, 0 if equal, 1 if a > b. Versions are strings like '1.2.3'."""
    va = parse_version(a)
    vb = parse_version(b)
    if va < vb:
        return -1
    elif va > vb:
        return 1
    else:
        return 0
