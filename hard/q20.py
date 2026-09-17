from abc import ABC, abstractmethod

# class Subscirber(ABC):
#     @abstractmethod
#     def update(self, temperature):
#         pass

# class PhoneDisplay(Subscirber):  # The observer
#     def __init__(self):
#         pass
#     def update(self, temperature):
#         print(f"Temperature updated to {temperature}")

# class TVDisplay(Subscirber):    # The observer
#     def __init__(self):
#         pass
#     def update(self, temperature):
#         print(f"Temperature updated to {temperature}")

# class WeatherStation:   # The subject
#     def __init__(self):
#         self._subscribers:list[Subscirber] = []

#     def attach(self, subscriber:Subscirber):
#         if subscriber not in self._subscribers:
#             self._subscribers.append(subscriber)

#     def set_temperature(self,temperature):
#         for subscriber in self._subscribers:
#             subscriber.update(temperature=temperature)

# station = WeatherStation()
# d1 = PhoneDisplay()
# d2 = TVDisplay()
# station.attach(d1)
# station.attach(d2)
# station.set_temperature(28)