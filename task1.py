from typing import Callable

def caching_fibonacci() -> Callable:
    cache = {}

    def fibonacci(n: int) -> int:
        try:
            if n <= 0:
                return 0
            if n == 1:
                return 1
            if n in cache:
                return cache[n]
            
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
            return cache[n]
        except TypeError:
            print("Passed argument should be of type int")
    
    return fibonacci


fib = caching_fibonacci()
print(fib(5))
print(fib(10))
print(fib(10))
print(fib('1'))
print(fib([]))
print(fib({}))