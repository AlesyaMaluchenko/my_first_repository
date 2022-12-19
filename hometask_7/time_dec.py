import time
from functools import lru_cache


def time_dec(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function(*args, **kwargs)
        return time.time() - start_time

    return wrapper


def fib1(n):
    if n == 1 or n == 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)


def fib2(n):
    n1 = 1
    n2 = 1
    for i in range(2, n):
        n1, n2 = n2, n1 + n2
    return n2


@lru_cache(maxsize=None)
def fib3(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib3(n - 1) + fib3(n - 2)


@time_dec
def fib1_time(n):
    return fib1(n)


@time_dec
def fib2_time(n):
    return fib2(n)


@time_dec
def fib3_time(n):
    return fib3(n)


print(fib1_time(35))
print(fib3_time(75))


