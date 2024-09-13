from .vehicle_type import VehicleType
from vehicle import Vehicle
class Motorcycle(Vehicle):
    def __init__(self, type: VehicleType, license_number):
        super().__init__(VehicleType.MOTORCYCLE, license_number)