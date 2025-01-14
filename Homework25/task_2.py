from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def move():
        pass


class Car(Vehicle):
    @staticmethod
    def move():
        print("The car is driving")


class Bike(Vehicle):
    @staticmethod
    def move():
        print("The bike is cycling")

    

class Truck(Vehicle):
    @staticmethod
    def move():
        print("The truck is hauling")


def test_vehicles(vehicles: list):
    for vehicle in vehicles:
        vehicle.move()


def main():
    car1 = Car()
    car2 = Car()
    bike1 = Bike()
    bike2 = Bike()
    truck1 = Truck()
    truck2 = Truck()
    vehicles = [car1, bike1, truck1, car2, bike2, truck2]
    test_vehicles(vehicles)


if __name__ == "__main__":
    main()

