from threading import Thread
from concurrent.futures import ProcessPoolExecutor as Pool
from utils import get_socket

pool = Pool(4)


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def work_server(address):
    sock = get_socket(address)
    while True:
        client, addr = sock.accept()
        print("connection", addr)
        Thread(target=work_handler, args=(client,)).start()


def work_handler(client):
    while True:
        try:
            req = client.recv(100)
        except ConnectionResetError:
            break
        if not req:
            break
        n = int(req)
        future = pool.submit(fib, n)
        r = future.result()
        resp = str(r).format(n).encode('ascii') + b'\n'
        client.send(resp)
    print("Socket closed")


work_server(('', 25000))
