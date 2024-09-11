# THERE IS ANOTHER LAYER OF ABSTRACTION AS COMPARED TO FACTORY METHOD
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
    
class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self):
        pass

class CarFactory(VehicleFactory):
    def create_vehicle(self):
        return Car()

class BikeFactory(VehicleFactory):
    def create_vehicle(self):
        return Bike()
    
def client_code(factory: VehicleFactory):
    vehicle = factory.create_vehicle()
    print(vehicle.create())

client_code(BikeFactory())
client_code(CarFactory())