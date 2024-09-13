# singleton
from level import Level
from vehicle_type import VehicleType
from vehicle import Vehicle
from typing import List
class ParkingLot:
    _instance = None

    def __init__(self) -> None:
        # is instance has already been created, raise error
        if self._instance is not None:
            raise Exception('This is Singleton class, as there can only be one parking lot')
        else:
            self._instance = self
            self.levels = List[Level] = []
        
    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            return ParkingLot()
        return ParkingLot._instance
        
    def add_level(self, level: Level):
        self.levels.append(level)

    def park_vehicle(self, vehicle: Vehicle):
        for level in self.levels:
            if level.parking_available(vehicle.get_type()):
                level.park_vehicle(vehicle)
                return True
        return False
    
    def unpark_vehicle(self, vehicle:  Vehicle):
        for level in self.levels:
            if level.unpark_vehicle(vehicle):
                return True
        return False