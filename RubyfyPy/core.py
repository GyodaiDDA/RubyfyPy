import collections

def is_hashable(obj) -> bool:
    return isinstance(obj, collections.abc.Hashable)
