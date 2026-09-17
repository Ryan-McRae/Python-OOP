# QUESTION 7
# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#     def total_pay(self):
#         return self.salary

# class Manager(Employee):
#     def __init__(self, name, salary, bonus):
#         self.bonus = bonus
#         super().__init__(name, salary)

#     def total_pay(self):
#         return super().total_pay() + self.bonus

# e = Employee("Thabo", 20000)
# m = Manager("Lindiwe", 25000, 5000)
# print(e.total_pay())
# print(m.total_pay())
