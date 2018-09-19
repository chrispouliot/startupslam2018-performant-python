def countdown(num):
    while num >= 0:
        yield num
        num -= 1


count = countdown(10)
for n in count:
    print(n)

# 10
# 9
# ...
