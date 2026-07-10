class Vehicle:
    def __init__(self, name , year):
        self.name = name 
        self.year = year

    def start(self):
        print("Vehicle starts..")
    def stop(self):
        print("Vehicle stops..")

class Car(Vehicle):
    def __init__(self, name, year , doors):
        super().__init__(name, year)
        self.doors = doors
class Bike(Vehicle):
    def __init__(self, name, year, price):
        super().__init__(name, year)
        self.price = price

car = Car("BMW", 2004, 2)
bike = Bike("Kawasaki Ninja H2r ",2004, 8000000 )

print(car.__dict__)
print(bike.__dict__)
bike.start()
car.stop()


vehicles = ["Bmw",2004,4]