class Bass(object):
    def __init__(self, name):
        print("------" + name + "--------")


class Subclass(Bass):
    def __init__(self, subname):
        Bass.__init__(self,subname)
        print(subname)


a = Subclass("老王")
