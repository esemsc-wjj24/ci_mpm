from functools import cache

__all__ = ["my_sum", "factorial"]


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return n * factorial(n - 1) if n else 1

def sin(x):
    num_of_terms = 20
    # use the taylor series expansion of sin(x)
    # sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
    for i in range(1, num_of_terms+1):
        if i % 2 == 0:
            x = x - (x**i)/factorial(i)
        else:
            x = x + (x**i)/factorial(i)
    