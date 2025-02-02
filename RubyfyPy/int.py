def is_prime(n: int) -> bool:
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    return False

def is_even(n: int) -> bool:
    return n % 2 == 0

def is_odd(n: int) -> bool:
    return n % 2 != 0