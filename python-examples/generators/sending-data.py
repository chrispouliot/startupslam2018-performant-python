def mult(m):
    while True:
        x = yield
        yield m * x


multiplier = mult(2)
next(multiplier)
print(multiplier.send(1))
next(multiplier)
print(multiplier.send(2))

# 2
# 4
