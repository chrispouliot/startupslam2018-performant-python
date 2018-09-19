def gen(f):
    return f


from random import randint

from tornado import ioloop
from tornado.httpclient import AsyncHTTPClient
from functools import partial

AsyncHTTPClient.configure("tornado.curl_httpclient.curlAsyncHTTPClient", max_clients=100)
url = "http://209.97.148.110"


def build_urls(url, count):
    for i in range(count):
        yield "{}/{}".format(url, randint(1, 1000))


@gen.coroutine
def main(base_url):
    http_client = AsyncHTTPClient()
    urls = build_urls(url, 100)
    responses = yield [http_client.fetch(u) for u in urls]
    raise gen.Return(value=responses)  # We cant return from a generator, we have to raise an exception!


if __name__ == "__main__":
    _ioloop = ioloop.IOLoop.instance()
    run_func = partial(main, url)
    result = _ioloop.run_sync(run_func)
    print(result)
