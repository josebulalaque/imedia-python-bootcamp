import time

print("Measuring Execution Time:")

print("Current Time:", time.ctime())
time.sleep(10)
print("Current Time:", time.ctime())
print()

print("Measuring Execution Time:")
start_time = time.time()
for _ in range(1_000_000):
    x = 10 ** 1000
end_time = time.time()
print(f"Spent {end_time - start_time:.5f} seconds")
