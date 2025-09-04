import time
from multiprocessing import Pool


def process(number):
    time.sleep(number)
    print("Finished")

if __name__ == "__main__":
    start_time = time.time()

    inputs = [5, 10, 15]
    with Pool() as pool:
        outputs = pool.map(process, inputs)

    end_time = time.time()
    print(end_time - start_time)
