def reader():
    # Read from a file, a socket, a database
    for i in range(4):
        yield '<< %s' % i


def reader_wrapper(g):
    yield from g


wrap = reader_wrapper(reader())
for i in wrap:
    print(i)

# << 0
# << 1
# ...


def writer():
    # Write to a file, a socket, a database
    while True:
        w = (yield)
        print('>> ', w)


def writer_wrapper(g):
    g.send(None)
    while True:
        try:
            x = (yield)  # Capture the value that's sent
            g.send(x)  # and pass it to the writer
        except StopIteration:
            pass


def better_writer_wrapper(g):
    yield from g

# >>  0
# >>  1
