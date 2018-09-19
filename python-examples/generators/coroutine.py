def generator():
    for i in range(1, 10):
        print("From generator {}".format((yield i)))


c = generator()
c.send(None)  # Prime the generator. Can't send normal data at first

while True:
    print("From user {}".format(c.send(1)))

# From generator 1
# From user 2
# From generator 1
# From user 3
# ...


def coroutine(f):
    return f


def slow():
    pass


@coroutine
def example():
    data = yield from slow()
    print(data)
