import time
from multiprocessing import Pool
from functools import cache

@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    start_time = time.time()

    inputs = [35, 36, 37, 38]
    with Pool() as pool:
        outputs = pool.map(fib, inputs)

    # outputs = [fib(number) for number in inputs]




    end_time = time.time()
    print(end_time - start_time)
