from cache_config import cache


@cache.memoize()
def fibonacci(n: int) -> int:
    #verificare daca rezultatul este deja in cache
    print(f"Calcul direct Fibonacci({n})")
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    prev = 0
    curr = 1

    for _ in range(2, n + 1):
        next_value = prev + curr
        prev = curr
        curr = next_value

    return curr
