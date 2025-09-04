import time


def process(number):
    time.sleep(10)
    print("Finished")


if __name__ == "__main__":
    start_time = time.time()

    inputs = [5, 10, 15]
    outputs = [process(number) for number in inputs]

    end_time = time.time()
    print(end_time - start_time)
