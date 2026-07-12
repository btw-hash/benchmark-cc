"""Geometry & arithmetic utility library.

A collection of small numerical helpers — distances, areas, statistical
aggregates, and combinatorics. All functions operate on plain numeric inputs.
"""

import math
from typing import Iterable, List, Sequence


def hypot_00(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_00(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_00(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_00(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_00(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_00(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_00(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_00(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_00(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_00(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_01(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_01(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_01(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_01(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_01(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_01(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_01(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_01(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_01(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_01(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_02(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_02(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_02(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_02(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_02(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_02(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_02(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_02(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_02(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_02(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_03(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_03(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_03(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_03(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_03(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_03(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_03(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_03(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_03(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_03(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_04(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_04(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_04(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_04(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_04(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_04(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_04(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_04(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_04(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_04(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_05(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_05(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_05(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_05(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_05(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_05(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_05(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_05(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_05(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_05(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_06(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_06(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_06(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_06(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_06(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_06(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_06(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_06(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_06(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_06(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_07(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_07(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_07(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_07(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_07(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_07(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_07(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_07(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_07(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_07(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_08(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_08(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_08(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_08(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_08(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_08(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_08(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_08(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_08(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_08(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_09(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_09(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_09(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_09(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_09(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_09(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_09(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_09(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_09(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_09(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_10(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_10(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_10(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_10(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_10(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_10(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_10(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_10(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_10(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_10(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_11(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_11(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_11(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_11(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_11(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_11(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_11(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_11(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_11(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_11(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_12(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_12(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_12(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_12(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_12(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_12(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_12(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_12(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_12(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_12(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_13(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_13(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_13(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_13(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_13(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_13(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_13(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_13(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_13(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_13(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_14(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_14(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_14(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_14(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_14(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_14(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_14(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_14(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_14(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_14(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def sum_of_00(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_00(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_00(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_00(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_00(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_00(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_00(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_00(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_00(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_00(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_01(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_01(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_01(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_01(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_01(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_01(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_01(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_01(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_01(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_01(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_02(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_02(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_02(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_02(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_02(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_02(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_02(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_02(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_02(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_02(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_03(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_03(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_03(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_03(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_03(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_03(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_03(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_03(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_03(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_03(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_04(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_04(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_04(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_04(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_04(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_04(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_04(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_04(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_04(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_04(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_05(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_05(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_05(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_05(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_05(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_05(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_05(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_05(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_05(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_05(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_06(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_06(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_06(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_06(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_06(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_06(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_06(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_06(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_06(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_06(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_07(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_07(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_07(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_07(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_07(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_07(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_07(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_07(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_07(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_07(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_08(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_08(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_08(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_08(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_08(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_08(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_08(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_08(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_08(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_08(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_09(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_09(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_09(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_09(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_09(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_09(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_09(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_09(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_09(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_09(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def factorial_00(n: int) -> int:
    """Return the factorial of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def triangular_00(n: int) -> int:
    """Return the triangular number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i
    return result


def square_pyramidal_00(n: int) -> int:
    """Return the square pyramidal number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i * i
    return result


def double_factorial_even_00(n: int) -> int:
    """Return the double factorial (even) of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * (i * 2) if i * 2 <= n else result
    return result


def factorial_01(n: int) -> int:
    """Return the factorial of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def triangular_01(n: int) -> int:
    """Return the triangular number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i
    return result


def square_pyramidal_01(n: int) -> int:
    """Return the square pyramidal number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i * i
    return result


def double_factorial_even_01(n: int) -> int:
    """Return the double factorial (even) of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * (i * 2) if i * 2 <= n else result
    return result


def factorial_02(n: int) -> int:
    """Return the factorial of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def triangular_02(n: int) -> int:
    """Return the triangular number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i
    return result


def square_pyramidal_02(n: int) -> int:
    """Return the square pyramidal number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i * i
    return result


def double_factorial_even_02(n: int) -> int:
    """Return the double factorial (even) of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * (i * 2) if i * 2 <= n else result
    return result


def factorial_03(n: int) -> int:
    """Return the factorial of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def triangular_03(n: int) -> int:
    """Return the triangular number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i
    return result


def square_pyramidal_03(n: int) -> int:
    """Return the square pyramidal number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i * i
    return result


def double_factorial_even_03(n: int) -> int:
    """Return the double factorial (even) of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * (i * 2) if i * 2 <= n else result
    return result


def factorial_04(n: int) -> int:
    """Return the factorial of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def triangular_04(n: int) -> int:
    """Return the triangular number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i
    return result


def square_pyramidal_04(n: int) -> int:
    """Return the square pyramidal number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i * i
    return result


def double_factorial_even_04(n: int) -> int:
    """Return the double factorial (even) of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * (i * 2) if i * 2 <= n else result
    return result


def factorial_05(n: int) -> int:
    """Return the factorial of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def triangular_05(n: int) -> int:
    """Return the triangular number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i
    return result


def square_pyramidal_05(n: int) -> int:
    """Return the square pyramidal number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i * i
    return result


def double_factorial_even_05(n: int) -> int:
    """Return the double factorial (even) of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * (i * 2) if i * 2 <= n else result
    return result


def factorial_06(n: int) -> int:
    """Return the factorial of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def triangular_06(n: int) -> int:
    """Return the triangular number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i
    return result


def square_pyramidal_06(n: int) -> int:
    """Return the square pyramidal number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i * i
    return result


def double_factorial_even_06(n: int) -> int:
    """Return the double factorial (even) of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * (i * 2) if i * 2 <= n else result
    return result


def factorial_07(n: int) -> int:
    """Return the factorial of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def triangular_07(n: int) -> int:
    """Return the triangular number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i
    return result


def square_pyramidal_07(n: int) -> int:
    """Return the square pyramidal number of n."""
    if n <= 1:
        return n
    result = 0
    for i in range(2, n + 1):
        result = result + i * i
    return result


def double_factorial_even_07(n: int) -> int:
    """Return the double factorial (even) of n."""
    if n <= 1:
        return n
    result = 1
    for i in range(2, n + 1):
        result = result * (i * 2) if i * 2 <= n else result
    return result


def percentile(values: Sequence[float], p: float) -> float:
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


def hypot_post_00(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_post_00(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_post_00(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_post_00(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_post_00(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_post_00(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_post_00(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_post_00(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_post_00(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_post_00(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_post_01(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_post_01(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_post_01(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_post_01(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_post_01(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_post_01(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_post_01(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_post_01(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_post_01(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_post_01(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_post_02(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_post_02(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_post_02(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_post_02(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_post_02(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_post_02(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_post_02(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_post_02(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_post_02(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_post_02(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_post_03(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_post_03(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_post_03(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_post_03(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_post_03(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_post_03(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_post_03(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_post_03(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_post_03(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_post_03(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_post_04(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_post_04(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_post_04(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_post_04(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_post_04(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_post_04(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_post_04(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_post_04(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_post_04(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_post_04(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_post_05(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_post_05(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_post_05(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_post_05(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_post_05(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_post_05(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_post_05(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_post_05(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_post_05(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_post_05(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_post_06(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_post_06(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_post_06(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_post_06(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_post_06(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_post_06(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_post_06(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_post_06(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_post_06(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_post_06(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_post_07(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_post_07(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_post_07(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_post_07(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_post_07(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_post_07(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_post_07(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_post_07(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_post_07(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_post_07(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_post_08(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_post_08(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_post_08(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_post_08(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_post_08(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_post_08(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_post_08(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_post_08(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_post_08(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_post_08(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def hypot_post_09(x: float, y: float) -> float:
    """Compute Euclidean distance for inputs x, y."""
    return math.sqrt(x ** 2 + y ** 2)


def manhattan_post_09(x: float, y: float) -> float:
    """Compute Manhattan distance for inputs x, y."""
    return abs(x) + abs(y)


def chebyshev_post_09(x: float, y: float) -> float:
    """Compute Chebyshev distance for inputs x, y."""
    return max(abs(x), abs(y))


def midpoint_x_post_09(x: float, y: float) -> float:
    """Compute x-midpoint for inputs x, y."""
    return (x + y) / 2


def avg_post_09(x: float, y: float) -> float:
    """Compute arithmetic mean for inputs x, y."""
    return (x + y) / 2


def geo_mean_post_09(x: float, y: float) -> float:
    """Compute geometric mean for inputs x, y."""
    return math.sqrt(x * y)


def harmonic_mean_post_09(x: float, y: float) -> float:
    """Compute harmonic mean for inputs x, y."""
    return 2 * x * y / (x + y) if (x + y) else 0


def rmse_pair_post_09(x: float, y: float) -> float:
    """Compute RMSE of a single pair for inputs x, y."""
    return math.sqrt(((x - y) ** 2) / 2)


def power_diff_post_09(x: float, y: float) -> float:
    """Compute absolute power difference for inputs x, y."""
    return abs(x ** 2 - y ** 2)


def log_ratio_post_09(x: float, y: float) -> float:
    """Compute log ratio for inputs x, y."""
    return math.log(x / y) if y else 0


def sum_of_post_00(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_post_00(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_post_00(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_post_00(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_post_00(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_post_00(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_post_00(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_post_00(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_post_00(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_post_00(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_post_01(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_post_01(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_post_01(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_post_01(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_post_01(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_post_01(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_post_01(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_post_01(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_post_01(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_post_01(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_post_02(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_post_02(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_post_02(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_post_02(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_post_02(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_post_02(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_post_02(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_post_02(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_post_02(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_post_02(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_post_03(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_post_03(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_post_03(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_post_03(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_post_03(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_post_03(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_post_03(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_post_03(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_post_03(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_post_03(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_post_04(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_post_04(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_post_04(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_post_04(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_post_04(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_post_04(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_post_04(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_post_04(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_post_04(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_post_04(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_post_05(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_post_05(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_post_05(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_post_05(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_post_05(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_post_05(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_post_05(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_post_05(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_post_05(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_post_05(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_post_06(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_post_06(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_post_06(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_post_06(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_post_06(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_post_06(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_post_06(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_post_06(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_post_06(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_post_06(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


def sum_of_post_07(values: Sequence[float]) -> float:
    """Return the sum of values."""
    if not values:
        return 0.0
    return sum(values)


def avg_of_post_07(values: Sequence[float]) -> float:
    """Return the average of values."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def max_of_post_07(values: Sequence[float]) -> float:
    """Return the max of values."""
    if not values:
        return 0.0
    return max(values)


def min_of_post_07(values: Sequence[float]) -> float:
    """Return the min of values."""
    if not values:
        return 0.0
    return min(values)


def range_of_post_07(values: Sequence[float]) -> float:
    """Return the range of values."""
    if not values:
        return 0.0
    return max(values) - min(values)


def mean_abs_post_07(values: Sequence[float]) -> float:
    """Return the mean absolute value of values."""
    if not values:
        return 0.0
    return sum(abs(v) for v in values) / len(values)


def sum_sq_post_07(values: Sequence[float]) -> float:
    """Return the sum of squares of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values)


def rms_post_07(values: Sequence[float]) -> float:
    """Return the root-mean-square of values."""
    if not values:
        return 0.0
    return math.sqrt(sum(v ** 2 for v in values) / len(values))


def mean_squared_post_07(values: Sequence[float]) -> float:
    """Return the mean square of values."""
    if not values:
        return 0.0
    return sum(v ** 2 for v in values) / len(values)


def product_post_07(values: Sequence[float]) -> float:
    """Return the product of values."""
    if not values:
        return 0.0
    return math.prod(values)


