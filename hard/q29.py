from __future__ import annotations
from abc import ABC, abstractmethod

# class Ticket:
#     def __init__(self, message:str, severity:int):
#         self.message = message
#         self.severity = severity

# class Handler(ABC):
#     @abstractmethod
#     def set_next(self, handler:Handler) -> Handler:
#         pass
#     @abstractmethod
#     def handle(self,ticket:Ticket):
#         pass

# class AbstractHandler(Handler):
#     _next_handler:Handler = None

#     # @abstractmethod
#     def set_next(self, handler:Handler):
#         self._next_handler = handler

#     @abstractmethod
#     def handle(self, ticket:Ticket):
#         if self._next_handler:
#             return self._next_handler.handle(ticket)

# class Level1Support(AbstractHandler):
#     SEVERITY = 3

#     def __init__(self, next):
#         if next is not None:
#             super().set_next(next)
#         else: 
#             super().set_next(self)
        
#     def handle(self, ticket:Ticket):
#         if ticket.severity < self.SEVERITY:
#             print(f"Level1 is resolving ticket: {ticket.message}")
#         else:
#             return super().handle(ticket=ticket)

# class Level2Support(AbstractHandler):
#     SEVERITY = 6
#     def __init__(self, next):
#         if next is not None:
#             super().set_next(next)
#         else: 
#             super().set_next(self)

#     def handle(self, ticket:Ticket):
#         if ticket.severity < self.SEVERITY:
#             print(f"Level2 is resolving ticket: {ticket.message}")
#         else:
#             return super().handle(ticket=ticket)

# class Level3Support(AbstractHandler):
#     SEVERITY = 10
#     def __init__(self, next):
#         if next is not None:
#             super().set_next(next)
#         else:
#             super().set_next(self)

#     def handle(self, ticket:Ticket):
#         if ticket.severity <= self.SEVERITY:
#             print(f"Level3 is resolving ticket: {ticket.message}")
#         else:
#             return super().handle(ticket=ticket)

# chain = Level1Support(Level2Support(Level3Support(None)))
# chain.handle(Ticket("Server down", severity=9))