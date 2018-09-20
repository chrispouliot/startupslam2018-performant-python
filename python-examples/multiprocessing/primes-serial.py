import math
import time


def is_prime(n):
    if not n % 2:
        return False
    start = 3
    to = math.sqrt(n) + 1
    for i in range(start, int(to), 2):
        if not n % i:
            return False
    return True


start_t = time.time()
for n in range(100000000, 101000000):
    is_prime(n)
print("Finished! Took: ", time.time() - start_t)
