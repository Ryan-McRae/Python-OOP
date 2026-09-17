from abc import ABC, abstractmethod

# class State(ABC):
#     @abstractmethod
#     def step_forward(self, traffic_state:TrafficLight):
#         pass

# class RedState(State):
#     KEY = "RED"
#     def step_forward(self, traffic_state:TrafficLight):
#         traffic_state.set_state(GreenState())

# class YellowState:
#     KEY = "YELLOW"
#     def step_forward(self, traffic_state:TrafficLight):
#         traffic_state.set_state(RedState())

# class GreenState:
#     KEY = "GREEN"
#     def step_forward(self, traffic_state:TrafficLight):
#         traffic_state.set_state(YellowState())

# class TrafficLight:
#     def __init__(self):
#         self._state = RedState()

#     def next(self):
#         self._state.step_forward(self)

#     def set_state(self,state):
#         self._state = state

#     def current_state(self):
#         return self._state.KEY

# light = TrafficLight()
# print(light.current_state())
# light.next()
# print(light.current_state())
# light.next()
# print(light.current_state())