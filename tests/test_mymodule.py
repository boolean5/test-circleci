import mymodule

def test_increment():
    """Test increment."""
    assert mymodule.increment(4) == 5

def test_decrement():
    """Test decrement."""
    assert mymodule.decrement(4) == 3

def test_double():
    """Test double."""
    assert mymodule.double(4) == 8

def test_is_greater_than():
    assert mymodule.is_greater_than(5, 4)
