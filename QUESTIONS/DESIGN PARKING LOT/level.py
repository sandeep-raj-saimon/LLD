from parking_spot import ParkingSpot
from vehicle import Vehicle
from vehicle_type import VehicleType
from typing import List
class Level:
    def __init__(self, number, num_parking_spots: int):
        self.level_number = number
        self.parking_spots = [ParkingSpot(i, self.level_number) for i in range(num_parking_spots)]
    
    def get_level_number(self):
        return self.level_number

    def parking_available(self, type: VehicleType):
        for spot in self.parking_spots:
            if spot.is_available == True and spot.get_type == type:
                return True
        return False

    def park_vehicle(self, vehicle: Vehicle):
        if self.parking_available:
            for spot in self.parking_spots:
                if spot.type == vehicle.get_type():
                    spot.park_vehicle = vehicle
                    return True
        return False
    
    def unpark_vehicle(self, vehicle: Vehicle):
        for spot in self.parking_spots:
            if spot.get_parked_vehicle == vehicle:
                spot.unpark_vehicle()
                return True
        return False

    
