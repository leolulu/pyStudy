def w1():
    def inner(whotodiao):
        if (whotodiao == "f1"):
            f1()
        if (whotodiao == "f2"):
            f2()

    return inner


def f1():
    print("----f1------")


def f2():
    print("-----f2-----")


innerFunc = w1()
innerFunc("f1")
