"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    x = num1 + num2
    return x


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    x = num1 - num2
    return x

def multiply(num1, num2):
    """Multiply the two inputs together."""
    x = num1 * num2
    return x

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    x = num1 / num2
    return x

def square(num1):
    """Return the square of the input."""
    x = num1 * num1
    return x

def cube(num1):
    """Return the cube of the input."""
    x = num1 ** 3
    return x

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    x = num1 ** num2
    return x        

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    x = num1 % num2
    return x

def add_mult(num1, num2, num3):
    x = (num1 + num2) * num3
    return x

def add_cubes(num1, num2):
    x = num1**3 + num2**3
    return x