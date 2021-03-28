
def add(x, y):
    """Add Function"""
    return x + y

def subtract(x, y):
    """Substract Function"""
    return x - y

def multiply(x, y):
    """Multiply Function"""
    return x * y

def devide(x, y):
    """Devide Function"""
    if y == 0:
        raise ValueError('Can not devide by zero!')
    return x / y