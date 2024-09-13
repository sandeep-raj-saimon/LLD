from vehicle_type import VehicleType
from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, type: VehicleType, license_number):
        self.license_number = license_number
        self.type = type

    def get_type(self):
        return self.type
    
