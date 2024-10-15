from functools import cache

__all__ = ["my_sum", "factorial", "sin"]


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1


def sin(x, num_of_terms=10):
    """Calculate sin(x) using Taylor series expansion"""
    sine = 0
    for k in range(num_of_terms):
        sign = (-1) ** k  # Alternating sign
        exponent = 2 * k + 1  # Exponents are odd numbers
        term = sign * x**exponent / factorial(exponent)
        sine += term
    return sine
