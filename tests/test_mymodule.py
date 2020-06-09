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
