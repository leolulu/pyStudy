def generator():
    for i in range(10000000000000):
        for j in (2,3):
            yield i*j

a = generator()

print(next(a))
print(last)#呵呵
print(next(a))
print(next(a))
