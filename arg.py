class Calculator:
    def add(self, *numbers):
        print(sum(numbers))

c1 = Calculator()
c1.add(10, 20)
c1.add(10, 20, 30)
c1.add(1, 2, 3, 4, 5)