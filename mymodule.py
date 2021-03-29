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
    """Do all the things."""
    return half(double(decrement(increment(x))))

def is_greater_than(x, y):
    result = False
    if x > y:
        result = True
    return result
