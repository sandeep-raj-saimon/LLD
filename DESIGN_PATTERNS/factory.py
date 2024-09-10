from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def create(self):
        pass

class Car(Vehicle):
    def create(self):
        return "car is created"
    
class Bike(Vehicle):
    def create(self):
        return "bike is created"
    
class VechileFactory:
    def get_vehicle(type):
        if type == 'car':
            return Car()
        elif type == 'bike':
            return Bike()
        else:
            raise ValueError("unknown vehicle type")

if __name__ == "__main__":
    type = 'car'
    vehicle = VechileFactory.get_vehicle(type)
    print(vehicle.create())

    type = 'bike'
    vehicle = VechileFactory.get_vehicle(type)
    print(vehicle.create())