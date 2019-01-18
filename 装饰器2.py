def decorator1(func):
    def temp_func():
        return func() * 2

    return temp_func


@decorator1
def func_plus(x, y):
    return x + y


result = func_plus(10, 20)
print(result)
