from socket import AF_INET, SOCK_STREAM, socket
from threading import Thread
import time


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))


def monitor():
    global n
    while True:
        time.sleep(1)
        print(n, 'reqs/s')
        n = 0


Thread(target=monitor).start()

n = 0
while True:
    sock.send(b'1')
    resp = sock.recv(100)
    n += 1
