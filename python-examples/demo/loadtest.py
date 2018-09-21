from socket import AF_INET, SOCK_STREAM, socket
import time


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))

while True:
    start = time.time()
    sock.send(b'1')
    resp = sock.recv(100)
    print(time.time() - start)
