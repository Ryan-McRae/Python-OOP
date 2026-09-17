# class Student:
#     def __init__(self, name:str):
#         self.name = name
#         self.courses = 0
#         self.grade = 0.0

#     def add_grade(self, grade:float):
#         self.courses+=1
#         self.grade+=grade

#     def average(self):
#         if self.courses != 0:
#             return self.grade/self.courses
#         return 0

# s = Student("Amahle")
# s.add_grade(80)
# s.add_grade(90)
# s.add_grade(70)
# print(s.average())