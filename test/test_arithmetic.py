# tests/test_arithmetic.py
import pytest
from pymath import add, subtract, multiply, divide


class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -2) == -3

    def test_floats(self):
        assert add(0.1, 0.2) == pytest.approx(0.3)  # ← important!


class TestSubtract:
    def test_basic(self):
        assert subtract(10, 4) == 6

    def test_result_is_negative(self):
        assert subtract(2, 5) == -3


class TestMultiply:
    def test_basic(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(99, 0) == 0


class TestDivide:
    def test_basic(self):
        assert divide(10, 2) == 5.0

    def test_returns_float(self):
        assert isinstance(divide(7, 2), float)

    def test_divide_by_zero_raises(self):
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            divide(5, 0)
