from random import randint
import time
import urllib2

from gevent import monkey
import gevent
monkey.patch_all()


url = "http://209.97.148.110"


def download(url):
    return urllib2.urlopen(url).read()


def build_urls(url, count):
    for i in range(count):
        yield "{}/{}".format(url, randint(1, 1000))


def main():
    requests = [gevent.spawn(download, u) for u in build_urls(url, 200)]  # Get's slower as we add more threads (200..300..400)
    gevent.joinall(requests)


if __name__ == '__main__':
    start = time.time()
    main()
    print("Elapsed: {}s".format(time.time() - start))
