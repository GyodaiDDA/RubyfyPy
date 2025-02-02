from RubyfyPy.int import is_prime, is_even, is_odd

def test_is_prime():
    # Test prime numbers
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(5) == True
    assert is_prime(7) == True
    assert is_prime(11) == True
    
    # Test non-prime numbers
    assert is_prime(1) == False
    assert is_prime(4) == False
    assert is_prime(6) == False
    assert is_prime(8) == False
    assert is_prime(9) == False
    
    # Test edge cases
    assert is_prime(0) == False
    assert is_prime(-1) == False

def test_is_even():
    assert is_even(2) == True
    assert is_even(4) == True
    assert is_even(0) == True
    assert is_even(-2) == True
    
    assert is_even(1) == False
    assert is_even(-1) == False
    assert is_even(3) == False

def test_is_odd():
    assert is_odd(1) == True
    assert is_odd(3) == True
    assert is_odd(-1) == True
    assert is_odd(-3) == True
    
    assert is_odd(2) == False
    assert is_odd(0) == False
    assert is_odd(-2) == False 