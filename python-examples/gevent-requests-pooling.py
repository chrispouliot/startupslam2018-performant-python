from random import randint
import time
import urllib2

from gevent import monkey, pool
import gevent
monkey.patch_all()


url = "http://209.97.148.110"


def download(url):
    urllib2.urlopen(url).read()


def build_urls(url, count):
    for i in range(count):
        yield "{}/{}".format(url, randint(1, 1000))


def main():
    p = pool.Pool(100)
    requests = [p.spawn(download, u) for u in build_urls(url, 500)]
    gevent.joinall(requests)


if __name__ == '__main__':
    start = time.time()
    main()
    print("Elapsed: {}s".format(time.time() - start))
