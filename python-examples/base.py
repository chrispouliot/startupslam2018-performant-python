from random import randint
import time

import requests

url = "http://209.97.148.110"


def build_urls(url, count):
    for i in range(count):
        yield f"{url}/{randint(1, 1000)}"


def main():
    for u in build_urls(url, 10):
        r = requests.get(u)
        print(r.status_code)


if __name__ == '__main__':
    start = time.time()
    main()
    print(f"Elapsed: {int(time.time() - start)}s")
