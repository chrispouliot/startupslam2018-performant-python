from random import randint
import asyncio
import aiohttp
import time

url = "http://209.97.148.110"


def build_urls(url, count):
    for i in range(count):
        yield "{}/{}".format(url, randint(1, 1000))


def chunked_http_client():
    semaphore = asyncio.Semaphore(100)  # 100 active threads

    @asyncio.coroutine
    def http_get(url):
        nonlocal semaphore  # enclosed scope variable
        with (yield from semaphore):
            r = yield from aiohttp.request('GET', url)
            data = yield from r.content.read()
            yield from r.wait_for_close()
        return data
    return http_get


def main(url):
    urls = build_urls(url, 500)
    http_client = chunked_http_client()
    tasks = [http_client(u) for u in urls]
    for future in asyncio.as_completed(tasks):
        data = yield from future
        print(data)
    return


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    start = time.time()
    loop.run_until_complete(main(url))
    print("Elapsed: {}s".format(time.time() - start))
