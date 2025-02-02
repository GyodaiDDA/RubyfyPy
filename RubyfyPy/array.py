def flatten(arr: list, bang: bool = False) -> list:
    result = []
    for item in arr:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    if bang:
        arr[:] = result
    return result

def last(arr: list) -> any:
    return arr[-1]

def first(arr: list) -> any:
    return arr[0]

def uniq(arr: list, bang: bool = False) -> list:
    from .core import is_hashable
    seen = set()
    result = []
    for item in arr:
        if is_hashable(item):
            if item not in seen:
                seen.add(item)
                result.append(item)
        else:
            if not any(item == i for i in result):
                result.append(item)
    if bang:
        arr[:] = result
    return result
