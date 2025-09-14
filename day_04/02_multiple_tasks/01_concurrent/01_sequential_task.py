import time

import requests


def fetch_url(url):
    return requests.get(url, verify=False).status_code


inputs = ['https://httpbin.org/delay/5', 'https://httpbin.org/delay/7']

#inputs = ['https://www.google.com']

if __name__ == '__main__':
    start_time = time.time()

    outputs = [fetch_url(url) for url in inputs]

    end_time = time.time()
    print(end_time - start_time)
