from cache_config import cache


@cache.memoize()
def calculate_power(base: int, exponent: int) -> int:
    return base ** exponent
