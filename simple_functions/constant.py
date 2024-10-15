from numpy import sqrt
from simple_functions.functions1 import factorial
from functools import cache

__all__ = ["pi"]


def pi(terms=1):
    return 1.0 / (2.0 * sqrt(2.0) / 9801.0 * rsum(terms))


@cache
def rsum(n):
    dividend = factorial(4 * n) * (1103 + 26390 * n)
    t = factorial(4 * n) * (1103 + 26390 * n) / dividend
    return t + rsum(n - 1) if n else t
