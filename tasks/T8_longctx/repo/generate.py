"""Generates a large synthetic module with one specific bug embedded.
Run once: `python generate.py`. Produces ./lib.py (~1500 lines, ~15-20K tokens).

This script is deliberately committed so the benchmark is reproducible across runners.
"""
import os

HEADER = '''"""Geometry & arithmetic utility library.

A collection of small numerical helpers — distances, areas, statistical
aggregates, and combinatorics. All functions operate on plain numeric inputs.
"""

import math
from typing import Iterable, List, Sequence


'''

# Templates for various plausible utility functions
TEMPLATES = [
    '''def {name}(x: float, y: float) -> float:
    """Compute {desc} for inputs x, y."""
    return {expr}


''',
    '''def {name}(values: Sequence[float]) -> float:
    """Return the {desc} of values."""
    if not values:
        return 0.0
    return {expr}


''',
    '''def {name}(n: int) -> int:
    """Return the {desc} of n."""
    if n <= 1:
        return n
    result = {init}
    for i in range(2, n + 1):
        result = {step}
    return result


''',
]

OPS = [
    ("hypot", "Euclidean distance", "math.sqrt(x ** 2 + y ** 2)"),
    ("manhattan", "Manhattan distance", "abs(x) + abs(y)"),
    ("chebyshev", "Chebyshev distance", "max(abs(x), abs(y))"),
    ("midpoint_x", "x-midpoint", "(x + y) / 2"),
    ("avg", "arithmetic mean", "(x + y) / 2"),
    ("geo_mean", "geometric mean", "math.sqrt(x * y)"),
    ("harmonic_mean", "harmonic mean", "2 * x * y / (x + y) if (x + y) else 0"),
    ("rmse_pair", "RMSE of a single pair", "math.sqrt(((x - y) ** 2) / 2)"),
    ("power_diff", "absolute power difference", "abs(x ** 2 - y ** 2)"),
    ("log_ratio", "log ratio", "math.log(x / y) if y else 0"),
]

AGGREGATES = [
    ("sum_of", "sum", "sum(values)"),
    ("avg_of", "average", "sum(values) / len(values)"),
    ("max_of", "max", "max(values)"),
    ("min_of", "min", "min(values)"),
    ("range_of", "range", "max(values) - min(values)"),
    ("mean_abs", "mean absolute value", "sum(abs(v) for v in values) / len(values)"),
    ("sum_sq", "sum of squares", "sum(v ** 2 for v in values)"),
    ("rms", "root-mean-square", "math.sqrt(sum(v ** 2 for v in values) / len(values))"),
    ("mean_squared", "mean square", "sum(v ** 2 for v in values) / len(values)"),
    ("product", "product", "math.prod(values)"),
]

ITERATIVE = [
    ("factorial", "factorial", "1", "result * i"),
    ("triangular", "triangular number", "0", "result + i"),
    ("square_pyramidal", "square pyramidal number", "0", "result + i * i"),
    ("double_factorial_even", "double factorial (even)", "1", "result * (i * 2) if i * 2 <= n else result"),
]


def emit():
    out = [HEADER]
    # Pairwise ops, many variations
    for i in range(15):
        for name, desc, expr in OPS:
            full_name = f"{name}_{i:02d}"
            out.append(TEMPLATES[0].format(name=full_name, desc=desc, expr=expr))
    # Aggregates over sequences
    for i in range(10):
        for name, desc, expr in AGGREGATES:
            full_name = f"{name}_{i:02d}"
            out.append(TEMPLATES[1].format(name=full_name, desc=desc, expr=expr))
    # Iterative computations
    for i in range(8):
        for name, desc, init, step in ITERATIVE:
            full_name = f"{name}_{i:02d}"
            out.append(TEMPLATES[2].format(name=full_name, desc=desc, init=init, step=step))

    # THE BUG: percentile function with off-by-one in index calculation.
    # Buried deep — line ~700+.
    out.append('''def percentile(values: Sequence[float], p: float) -> float:
    """Return the p-th percentile (0 <= p <= 100) of values, using the nearest-rank method.

    For N items, the index is ceil(p / 100 * N) - 1, clamped to [0, N-1].
    """
    if not values:
        return 0.0
    if not 0 <= p <= 100:
        raise ValueError("p must be between 0 and 100")
    s = sorted(values)
    # BUG: off-by-one — using floor instead of ceil, and missing the -1.
    idx = int(p / 100 * len(s))
    if idx >= len(s):
        idx = len(s) - 1
    return s[idx]


''')

    # More noise after the bug to make it harder to find by position alone
    for i in range(10):
        for name, desc, expr in OPS:
            full_name = f"{name}_post_{i:02d}"
            out.append(TEMPLATES[0].format(name=full_name, desc=desc, expr=expr))
    for i in range(8):
        for name, desc, expr in AGGREGATES:
            full_name = f"{name}_post_{i:02d}"
            out.append(TEMPLATES[1].format(name=full_name, desc=desc, expr=expr))

    return "".join(out)


if __name__ == "__main__":
    content = emit()
    path = os.path.join(os.path.dirname(__file__), "lib.py")
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    lines = content.count("\n")
    print(f"Wrote {path}: {lines} lines, ~{len(content)} chars")
