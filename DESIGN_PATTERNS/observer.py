# BEHAVIOURAL DESIGN PATTERN, WHEN SUBJECT CHANGES ITS STATE, OBSERVERS NEEDS TO GET NOTIFIED
from abc import ABC, abstractmethod
class WeatherStation:
    def __init__(self):
        self.observers = []
        self.temperature = None

    def add_observer(self, observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)
    
    def set_temperature(self, temperature):
        self.temperature = temperature
        self.notify_observers()

class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

class PhoneDisplay(Observer):
    def update(self, temperature):
        print(f'phone display temperature is {temperature}')
    
class WindowDisplay(Observer):
    def update(self, temperature):
         print(f'window display temperature is {temperature}')

if __name__ == "__main__":
    weather_station = WeatherStation()
    phone_display = PhoneDisplay()
    window_display = WindowDisplay()

    weather_station.add_observer(phone_display)
    weather_station.add_observer(window_display)

    weather_station.set_temperature(25)

    weather_station.remove_observer(phone_display)
    weather_station.set_temperature(30)