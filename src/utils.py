def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

#Added error handling for division by zero
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b