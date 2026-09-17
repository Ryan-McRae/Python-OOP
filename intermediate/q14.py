# QUESTION 14
# class Circle:
#     def __init__(self, radius:float):
#         self._radius = radius

#     @property
#     def radius(self):
#         return self._radius

#     @radius.setter
#     def radius(self, value):
#         if value < 0:
#             raise ValueError
#         else:
#             self._radius = value

#     @property
#     def area(self):
#         return 3.141 * (self.radius ** 2)
    
# c = Circle(5)
# print(round(c.area, 2))
# c.radius = -3