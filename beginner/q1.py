# # QUESTION 1
# class BankAccount:
#     def __init__(self, name:str, balance:float):
#         self.account_holder = name
#         self.balance        = balance

#     def deposit(self,amount:float):
#         self.balance += amount

#     def withdraw(self, amount:float):
#         if self.balance - amount >= 0:
#             self.balance -= amount
#         else:
#             print("Insuffecient funds.")

# acc = BankAccount("Sipho", 100)
# acc.deposit(50)
# acc.withdraw(30)
# acc.withdraw(1000)
# print(acc.balance)