'''
class calculator:
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        print(a + b + c)

c1 = calculator()
c1.add(10, 20)  '''

class calculator:
    def add(self, a, b, c=0):
        print(a + b + c)

c1 = calculator()
c1.add(10, 20)
c1.add(10, 20, 30)