from typing import Callable


def caching_fibonacci() -> Callable[[int], int]:
    cache = {}

    def fibonacci(n: int) -> int:
        # bool is a subclass of int, so reject it explicitly
        if not isinstance(n, int) or isinstance(n, bool):
            raise TypeError(f"Argument must be an integer, got {type(n).__name__}")
        if n < 0:
            raise ValueError("Argument must be a non-negative integer")

        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


if __name__ == "__main__":
    fib = caching_fibonacci()
    print(fib(5))   # 5
    print(fib(10))  # 55
    print(fib(10))  # 55 (from cache)

    for bad_value in ['1', [], {}, 2.5, True, -3]:
        try:
            fib(bad_value)
        except (TypeError, ValueError) as error:
            print(f"fib({bad_value!r}) -> Error: {error}")
