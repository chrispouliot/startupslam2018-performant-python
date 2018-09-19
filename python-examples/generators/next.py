def countdown(num):
    while num >= 0:
        yield num
        num -= 1


count = countdown(10)
print(next(count))
print(next(count))
print(next(count))

# 10
# 9
# ...
