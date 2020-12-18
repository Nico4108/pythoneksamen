import math


class Triangle:
    def __init__(self):
        self.a = 30
        self.b = 30
        self.__c = 0

    @property
    def c(self):
        return math.sqrt(self.a ** 2 + self.b ** 2)

    @c.setter
    def c(self, x):
        print('WARNING: C is can not be se')


t = Triangle()

# udkommenter @property og @c.setter og giv t.c en værdig (t.c(5))
# for at vise man ikke kan tilgå __c
print(t.a, t.b, t.c)
