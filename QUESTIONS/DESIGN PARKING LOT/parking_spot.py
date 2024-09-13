from .level import Level
from .vehicle_type import VehicleType
from .vehicle import Vehicle
class ParkingSpot:
    def __init__(self, level: Level, type: VehicleType, spot_number):
        self.spot_number = spot_number
        self.level = level
        self.type = (type or VehicleType.CAR) # keeping default type as CAR
        self.vehicle_parked = None # by default no vehicle is parked

    def is_available(self):
        return self.vehicle_parked

    def park_vehicle(self, vehicle: Vehicle):
        self.vehicle_parked = vehicle
    

    def unpark_vehicle(self):
        self.vehicle_parked = None
    
    def get_type(self):
        return self.type

    def get_parked_vehicle(self):
        return self.vehicle_parked


        