"""
Calculator module - basic arithmetic operations.
"""

def add(a: int, b: int) -> int:
    """Add two numbers and return the result."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract b from a and return the result."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers and return the result."""
    return a * b


def divide(a: int, b: int) -> float:
    """Divide a by b. Raises an error if b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Yeh calculator.py se print ho raha hai")
