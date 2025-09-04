import time
from functools import cache

print("Measuring Execution Time:")
start = time.time()


def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(38))

end = time.time()
print(end - start)

print("Measuring Execution Time:")
start = time.time()


@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(300))

end = time.time()
print(end - start)
