"""Errors for boundary layers.

Keep operator-core free of exceptions that encode I/O concerns.
"""

class OperatorsError(Exception):
    """Base error for operators package."""

class InputShapeError(OperatorsError):
    """Raised when input data does not match the expected shape."""
