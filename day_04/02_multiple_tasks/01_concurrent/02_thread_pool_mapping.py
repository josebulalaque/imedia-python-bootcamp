import time
from concurrent.futures import ThreadPoolExecutor

import requests


def fetch_url(url):
    return requests.get(url).status_code


inputs = ['https://httpbin.org/delay/5', 'https://httpbin.org/delay/7']

if __name__ == '__main__':
    start_time = time.time()

    with ThreadPoolExecutor() as executor:
        outputs = executor.map(fetch_url, inputs)

    end_time = time.time()
    print(end_time - start_time)
