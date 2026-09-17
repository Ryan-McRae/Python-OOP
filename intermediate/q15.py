# QUESTION 15
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Inventory:
    def __init__(self):
        self.items: dict[str,Item] = {}
    def add_item(self, item:Item):
        self.items[item.name] = item
    def remove_item(self, name):
        if name in self.items.keys():
            self.items.pop(name)
        else:
            pass
    def total_value(self):
        total_value = 0.0
        for k,v in self.items.items():
            total_value += (v.price * v.quantity) 
        return total_value

inv = Inventory()
inv.add_item(Item("Pen", 5, 10))
inv.add_item(Item("Notebook", 20, 3))
print(inv.total_value())
inv.remove_item("Pen")
print(inv.total_value())
