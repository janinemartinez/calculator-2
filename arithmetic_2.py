"""Math functions for calculator."""


def add(tokens):
    """Return the sum of the two inputs."""
    x = 0
    for i in range(len(tokens)):
        if i > 0:
            x += tokens[i]
       # if type(i) == type(float)
        #    x += i
    return x


def subtract(tokens):
    """Return the second number subtracted from the first."""
    x = tokens[1]
    for i in range(len(tokens)):
        if i > 1:
            x -= tokens[i]
    return x

def multiply(tokens):
    """Multiply the two inputs together."""

    x = 1
    for i in range(len(tokens)):
        if i > 0:
            x *= tokens[i]
    return x

def divide(tokens):
    """Divide the first input by the second and return the result."""
    x = tokens[1]
    for i in range(len(tokens)):
        if i > 1:
            x = x / tokens[i]
    return x

def square(tokens):
    """Return the square of the input."""
    x = []
    for i in range(len(tokens)):
        if i > 0:
            y = tokens[i] * tokens[i]
            x.append(y)
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