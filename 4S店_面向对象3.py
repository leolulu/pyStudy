class TestClass(object):
    def __init__(self):
        print("begin")

    def __del__(self):
        print("OVER")

    def __str__(self):
        return "TestClass"


a = TestClass()
print(a)
