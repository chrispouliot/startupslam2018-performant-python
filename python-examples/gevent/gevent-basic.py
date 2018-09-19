import gevent


def foo():
    print('Im in foo!')
    gevent.sleep(0)
    print('End of foo')


def bar():
    print('Im in bar')
    gevent.sleep(0)
    print('End of bar')


gevent.joinall([
    gevent.spawn(foo),  # Run foo in a greenlet
    gevent.spawn(bar),  # Run bar in a greenlet
])

# Im in foo!
# Im in bar
# End of foo
# End of bar
