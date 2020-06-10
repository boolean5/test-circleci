from myothermodule import half

def increment(x):
    """Increment."""
    return x + 1

def decrement(x):
    """Decrement."""
    return x - 1

def double(x):
    """Double."""
    return x * 2

def do_all(x):
    return half(double(decrement(increment(x))))

def is_greater_than(x, y):
    if x > y:
        return True
    return False
