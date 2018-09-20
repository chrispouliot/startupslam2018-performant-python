import math
import multiprocessing
import time


NUM_PROCESSES = 2
FLAG_DONE = b"DONE"
FLAG_FINISHED_PROCESSING = b"DONE_PROCESSING"


def is_prime(input_queue, prime_queue):
    while True:
        n = input_queue.get()
        if n == FLAG_DONE:
            prime_queue.put(FLAG_FINISHED_PROCESSING)
            break
        else:
            if not n % 2:
                continue
            for i in range(3, int(math.sqrt(n) + 1), 2):
                if not n % i:
                    break
            else:
                prime_queue.put(n)


if __name__ == "__main__":
    primes = []

    manager = multiprocessing.Manager()
    input_queue = manager.Queue()
    output_queue = manager.Queue()

    pool = multiprocessing.Pool(processes=NUM_PROCESSES)
    for _ in range(NUM_PROCESSES):
        p = multiprocessing.Process(target=is_prime, args=(input_queue, output_queue))
        p.start()

    start_time = time.time()
    num_range = range(100000000, 101000000)

    for possible_prime in num_range:
        input_queue.put(possible_prime)
    for n in range(NUM_PROCESSES):
        input_queue.put(FLAG_DONE)

    num_finished = 0
    while True:
        result = output_queue.get()
        if result == FLAG_FINISHED_PROCESSING:
            num_finished += 1
            if num_finished == NUM_PROCESSES:
                break
        else:
            primes.append(result)

    print("Finished! Took: ", time.time() - start_time)
