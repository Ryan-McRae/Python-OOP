# class A:
#     def greet(self):
#         return "A"
# class B(A):
#     def greet(self):
#         return "B"
# class C(A):
#     def greet(self):
#         return "C"
# class D(B,C):
#     def greet(self):
#         return super().greet()
# print(D().greet())
# print([cls.__name__ for cls in D.__mro__])