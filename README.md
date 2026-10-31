# Python Calculator

A small command-line calculator written in Python. It supports addition,
subtraction, multiplication, and division.

## Requirements

- Python 3
- `pytest` to run the tests

## Run the calculator

From the project directory, run:

```powershell
python calculator.py
```

Enter two numbers and an operation (`+`, `-`, `*`, or `/`) when prompted.
Division by zero and unsupported operations display an error message.

## Known limitation

Entering text that cannot be converted to a number may produce a Python
traceback.

## Run the tests

Install pytest if it is not already installed:

```powershell
python -m pip install pytest
```

Then run the test suite:

```powershell
python -m pytest
```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
