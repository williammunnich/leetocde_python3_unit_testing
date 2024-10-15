# math_operations.py
def add(a, b):
    """
    Function that returns the sum of two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Function that returns the difference of two numbers.
    Raises NotImplementedError if the function is not implemented.
    """
    raise NotImplementedError("subtract function not yet implemented")

def multiply(a, b):
    """
    Function that returns the product of two numbers.
    Raises NotImplementedError if the function is not implemented.
    """
    raise NotImplementedError("multiply function not yet implemented")

def divide(a, b):
    """
    Function that returns the quotient of two numbers.
    Raises ZeroDivisionError if the second argument is zero.
    """
    if b == 0:
        raise Exception("cannot divide by zero")
    return a / b
