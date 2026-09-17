# class VendingMachineError(BaseException):
#     pass

# class OutOfStockError(VendingMachineError):
#     pass

# class InsufficientFundsError(VendingMachineError):
#     def __init__(self, deficit, item):
#         self.deficit = deficit
#         self.item = item
#     def __str__(self):
#         return f"Need {self.deficit} more to purchase {self.item}"

# class VendingMachine:           # name, quant, price
#     def __init__(self, stock:dict[str,tuple[int, float]]):
#         self.stock = stock
        
#     def purchase(self, name, price):
#         if name in self.stock.keys():
#             item_price = self.stock[name][1]
#             if price < item_price:
#                 raise InsufficientFundsError(abs(price-item_price),name)
#         else:
#             raise OutOfStockError
# vm = VendingMachine({"Coke": (2, 15)})  # (stock, price)
# vm.purchase("Coke", 10)