# # QUESTION 10
# class Temperature:
#     celsius = 0

#     @classmethod
#     def from_fahrenheit(cls, f):
#         cls.celsius = (f - 32)*(5/9)
#         return cls

#     @staticmethod
#     def is_freezing(celsius):
#         if celsius < 0:
#             return True
#         return False

# t = Temperature.from_fahrenheit(98.6)
# print(round(t.celsius, 1))
# print(Temperature.is_freezing(-5))
