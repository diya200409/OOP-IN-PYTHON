class animal:
    def sound(self):
        print("Animal makes sound ")

class Dog(animal):
    def sound(self):
        print("barks ")

class Cat(animal):
    def sound(self):
        print("meows ")

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()