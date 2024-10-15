import pytest
import numpy as np
from simple_functions import my_sum, factorial, sin


class TestSimpleFunctions(object):
    """Class to test our simple functions are working correctly"""

    @pytest.mark.parametrize(
        "iterable, expected", [([8, 7, 5], 20), ((10, -2, 5, -10, 1), 4)]
    )
    def test_my_add(self, iterable, expected):
        """Test our add function"""
        isum = my_sum(iterable)
        assert isum == expected

    @pytest.mark.parametrize("number, expected", [(5, 120), (3, 6), (1, 1)])
    def test_factorial(self, number, expected):
        """Test our factorial function"""
        answer = factorial(number)
        assert answer == expected

    @pytest.mark.parametrize(
        "x, expected",
        [
            (0, 0.0),
            (np.pi / 6, 0.5),
            (np.pi / 4, np.sqrt(2) / 2),
            (np.pi / 3, np.sqrt(3) / 2),
            (np.pi / 2, 1.0),
            (np.pi, 0.0),
            (3 * np.pi / 2, -1.0),
            (-np.pi / 2, -1.0),
        ],
    )
    def test_sin(self, x, expected):
        """Test our sin function"""
        result = sin(x, num_of_terms=10)
        assert np.isclose(
            result, expected, atol=1e-7
        ), f"sin({x}) = {result}, expected {expected}"
