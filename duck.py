class Duck:

    def sound(self):
        print("Quack Quack")


class Dog:

    def sound(self):
        print("Bhow Bhow")


def make_sound(animal):
    animal.sound()


d1 = Duck()
d2 = Dog()

make_sound(d1)
make_sound(d2)
