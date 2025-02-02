from RubyfyPy.core import is_hashable

def test_is_hashable():
    # Test hashable types
    assert is_hashable(42) == True
    assert is_hashable("string") == True
    assert is_hashable((1, 2, 3)) == True
    assert is_hashable(None) == True
    
    # Test unhashable types
    assert is_hashable([1, 2, 3]) == False
    assert is_hashable({1: 2}) == False
    assert is_hashable(set([1, 2])) == False 