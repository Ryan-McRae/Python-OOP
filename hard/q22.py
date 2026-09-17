# class TypedProperty:
#     def __set_name__(self, owner, name):
#         self._name = f"_{name}"

#     def __get__(self, instance, owner):
#         if instance is None:
#             return self
#         return getattr(instance, self._name, None)
    
#     def __set__(self, instance, value):
#         if "age" in self._name:
#             if isinstance(value, int):
#                 setattr(instance, self._name, value)
#             else:
#                 raise TypeError
#         else:
#             setattr(instance, self._name, value)

# class Person:
#     name = TypedProperty()
#     age = TypedProperty()
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p = Person("Zanele", 25)
# p.age = "old"