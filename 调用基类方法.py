class Jilei(object):
    def __init__(self, name):
        self.name = name


class Zilei(Jilei):
    def __init__(self, name):
        super().__init__(name)


zilei_a = Zilei("小明活")

print(zilei_a.name)
