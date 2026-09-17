# class Shape:
#     pass

# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#     def area(self):
#         return 3.141 * (self.radius ** 2)

# class Square(Shape):
#     def __init__(self, length):
#         self.length = length
#     def area(self):
#         return self.length**2

# class Triangle(Shape):
#     def __init__(self, side1, side2,side3):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3
#     def area(self):
#         pass

# class ShapeFactory:
#     _registry = {
#         "circle":Circle,
#         "square":Shape,
#         "triangle":Triangle
#     }
#     @classmethod
#     def create_shape(cls,shape_type, **kwargs):
#         shape = cls._registry.get(shape_type.lower())
#         if not shape:
#             raise ValueError("Unknown shape type: hexagon")
#         return shape(**kwargs)
    
# s = ShapeFactory.create_shape("circle", radius=4)
# print(type(s).__name__)
# print(round(s.area(), 2))
# ShapeFactory.create_shape("hexagon")