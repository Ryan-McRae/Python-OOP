from abc import ABC, abstractmethod

# class PaymentMethod(ABC):
#     # def __int__(self):
#     #     raise TypeError

#     @abstractmethod
#     def pay(self, amount):
#         pass

# class CreditCard(PaymentMethod):
#     def pay(self, amount):
#         surcharge = 1.2
#         amount = amount + surcharge
#         return f"Paid {amount} with credit card."

# class CryptoWallet(PaymentMethod):
#     def pay(self, amount):
#         return f"Paid {amount} with crypto wallet."

# pm = PaymentMethod()