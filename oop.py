class Car:
    def __init__(self, brand):
        self.brand = brand

    def start(self):
        print("Car is starting")

class PetrolCar(Car):
    def start(self):
        print("Petrol engine started")

class ElectricCar(Car):
    def start(self):
        print("Electric motor started")

cars = [PetrolCar("BMW"), ElectricCar("Tesla")]
for car in cars:
    car.start()