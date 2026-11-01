import pytest

from calculator import calculate, get_number


def test_addition():
    assert calculate(10, 5, "+") == 15


def test_subtraction():
    assert calculate(10, 5, "-") == 5


def test_multiplication():
    assert calculate(10, 5, "*") == 50


def test_division():
    assert calculate(10, 5, "/") == 2


def test_division_by_zero():
    with pytest.raises(ZeroDivisionError):
        calculate(10, 0, "/")


def test_invalid_operation():
    with pytest.raises(ValueError):
        calculate(10, 5, "%")


def test_get_number_invalid_input(monkeypatch, capsys):
    inputs = iter(["cat", "5.5"])
    monkeypatch.setattr("builtins.input", lambda prompt: next(inputs))

    assert get_number("Enter X: ") == 5.5
    assert "Invalid input" in capsys.readouterr().out
