import pytest
from RubyfyPy.array import flatten, last, first, uniq

def test_flatten():
    # Test basic flattening
    assert flatten([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
    
    # Test empty list
    assert flatten([]) == []
    
    # Test bang operation
    arr = [1, [2, 3], [4, [5, 6]]]
    flatten(arr, bang=True)
    assert arr == [1, 2, 3, 4, 5, 6]

def test_last():
    assert last([1, 2, 3]) == 3
    assert last(['a', 'b', 'c']) == 'c'
    
    with pytest.raises(IndexError):
        last([])

def test_first():
    assert first([1, 2, 3]) == 1
    assert first(['a', 'b', 'c']) == 'a'
    
    with pytest.raises(IndexError):
        first([])

def test_uniq():
    # Test with hashable items
    assert uniq([1, 2, 2, 3, 3, 3]) == [1, 2, 3]
    
    # Test with unhashable items
    assert uniq([[1], [1], [2], [2, 3], [2, 3]]) == [[1], [2], [2, 3]]
    
    # Test mixed types
    assert uniq([1, 2, [1], [1], 2, 3]) == [1, 2, [1], 3]
    
    # Test bang operation
    arr = [1, 2, 2, 3, 3, 3]
    uniq(arr, bang=True)
    assert arr == [1, 2, 3] 