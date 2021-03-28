""" Mathametic functions """

def add(x_1, y_1):
    """Add Function"""
    return x_1 + y_1

def subtract(x_1, y_1):
    """Substract Function"""
    return x_1 - y_1

def multiply(x_1, y_1):
    """Multiply Function"""
    return x_1 * y_1

def devide(x_1, y_1):
    """Devide Function"""
    if y_1 == 0:
        raise ValueError('Can not devide by zero!')
    return x_1 / y_1
