# Python OOP Challenges (30 Total)

**5 Beginner · 10 Intermediate · 15 Advanced**

Each challenge describes the task, the classes/behavior you need to build, and gives sample input/output so you know what "correct" looks like. No solution code is provided — that part's on you.

---

## 🟢 BEGINNER (1–5)

### 1. The `BankAccount` Class
Create a `BankAccount` class that stores an account holder's name and balance. It should support depositing and withdrawing money, and should refuse to withdraw more than the current balance (print an error instead of crashing).

**Example:**
```
acc = BankAccount("Sipho", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(1000)
print(acc.balance)
```
**Expected Output:**
```
Insufficient funds.
120
```

---

### 2. The `Rectangle` Class
Build a `Rectangle` class with `width` and `height`. It should have methods to calculate area and perimeter.

**Example:**
```
r = Rectangle(4, 5)
print(r.area())
print(r.perimeter())
```
**Expected Output:**
```
20
18
```

---

### 3. The `Dog` Class with Attributes and a Method
Create a `Dog` class with `name` and `age` attributes and a `bark()` method that returns a string.

**Example:**
```
d = Dog("Rex", 3)
print(d.bark())
print(f"{d.name} is {d.age} years old")
```
**Expected Output:**
```
Rex says Woof!
Rex is 3 years old
```

---

### 4. `Student` Grade Tracker
Create a `Student` class that stores a name and a list of grades. Add a method `average()` that returns the average grade, and a method `add_grade(grade)` to append new grades.

**Example:**
```
s = Student("Amahle")
s.add_grade(80)
s.add_grade(90)
s.add_grade(70)
print(s.average())
```
**Expected Output:**
```
80.0
```

---

### 5. Basic Inheritance: `Animal` → `Cat`
Create an `Animal` base class with a `speak()` method that returns `"..."`. Create a `Cat` subclass that overrides `speak()` to return `"Meow"`.

**Example:**
```
a = Animal()
c = Cat()
print(a.speak())
print(c.speak())
```
**Expected Output:**
```
...
Meow
```

---

## 🟡 INTERMEDIATE (6–15)

### 6. `Shape` Hierarchy with Polymorphism
Create an abstract-ish `Shape` base class with an `area()` method that raises `NotImplementedError`. Create `Circle` and `Square` subclasses that implement `area()` properly. Then loop through a list of mixed shapes and print each area.

**Example:**
```
shapes = [Circle(3), Square(4)]
for s in shapes:
    print(round(s.area(), 2))
```
**Expected Output:**
```
28.27
16
```

---

### 7. `Employee` and `Manager` with `super()`
Create an `Employee` class with `name` and `salary`. Create a `Manager` subclass that adds a `bonus` attribute, uses `super().__init__()` to reuse the parent constructor, and overrides a `total_pay()` method to include the bonus.

**Example:**
```
e = Employee("Thabo", 20000)
m = Manager("Lindiwe", 25000, 5000)
print(e.total_pay())
print(m.total_pay())
```
**Expected Output:**
```
20000
30000
```

---

### 8. Operator Overloading: `Vector2D`
Create a `Vector2D` class with `x` and `y`. Overload the `+`, `-`, and `==` operators using dunder methods (`__add__`, `__sub__`, `__eq__`). Also implement `__repr__` so printing looks clean.

**Example:**
```
v1 = Vector2D(2, 3)
v2 = Vector2D(1, 1)
print(v1 + v2)
print(v1 - v2)
print(v1 == Vector2D(2, 3))
```
**Expected Output:**
```
Vector2D(3, 4)
Vector2D(1, 2)
True
```

---

### 9. Encapsulation: `Password`-Protected Attribute
Create a `SecureFile` class where `content` is a "private" attribute (name-mangled with `__content`). Provide a `read(password)` method that only returns the content if the correct password is given, otherwise returns `"Access Denied"`.

**Example:**
```
f = SecureFile("secretdata", "1234")
print(f.read("wrong"))
print(f.read("1234"))
```
**Expected Output:**
```
Access Denied
secretdata
```

---

### 10. Class Methods and Static Methods: `Temperature`
Create a `Temperature` class storing degrees in Celsius. Add a `@classmethod` `from_fahrenheit(f)` that constructs a `Temperature` object from a Fahrenheit value, and a `@staticmethod` `is_freezing(celsius)` that returns `True`/`False`.

**Example:**
```
t = Temperature.from_fahrenheit(98.6)
print(round(t.celsius, 1))
print(Temperature.is_freezing(-5))
```
**Expected Output:**
```
37.0
True
```

---

### 11. `Library` and `Book` Composition
Create a `Book` class with `title` and `is_checked_out`. Create a `Library` class that holds a list of `Book` objects, with methods `checkout(title)` and `return_book(title)` that update the correct book's status.

**Example:**
```
lib = Library()
lib.add_book(Book("Dune"))
lib.checkout("Dune")
print(lib.books[0].is_checked_out)
lib.return_book("Dune")
print(lib.books[0].is_checked_out)
```
**Expected Output:**
```
True
False
```

---

### 12. Multiple Inheritance: `Flyer` and `Swimmer`
Create two mixin classes, `Flyer` (with `fly()`) and `Swimmer` (with `swim()`). Create a `Duck` class that inherits from both, and can therefore do both actions.

**Example:**
```
d = Duck()
print(d.fly())
print(d.swim())
```
**Expected Output:**
```
Flying high!
Swimming gracefully!
```

---

### 13. Custom Iterable: `Playlist`
Create a `Playlist` class that stores a list of song names and implements `__iter__` and `__len__` so you can loop over it directly and call `len()` on it.

**Example:**
```
p = Playlist(["Song A", "Song B", "Song C"])
for song in p:
    print(song)
print(len(p))
```
**Expected Output:**
```
Song A
Song B
Song C
3
```

---

### 14. Property Decorators: `Circle` with Validation
Create a `Circle` class with a `radius` property. Use `@property` and a setter so that setting a negative radius raises a `ValueError`, while a valid radius updates correctly. Also add a computed `area` property (no parentheses needed to call it).

**Example:**
```
c = Circle(5)
print(round(c.area, 2))
c.radius = -3
```
**Expected Output:**
```
78.54
ValueError: Radius cannot be negative
```

---

### 15. `Inventory` System with Dictionaries of Objects
Create an `Item` class (`name`, `price`, `quantity`) and an `Inventory` class that stores items in a dictionary keyed by name. Add methods `add_item()`, `remove_item(name)`, and `total_value()` that sums `price * quantity` across all items.

**Example:**
```
inv = Inventory()
inv.add_item(Item("Pen", 5, 10))
inv.add_item(Item("Notebook", 20, 3))
print(inv.total_value())
inv.remove_item("Pen")
print(inv.total_value())
```
**Expected Output:**
```
110
60
```

---

## 🔴 ADVANCED (16–30)

### 16. Abstract Base Classes with `abc` Module
Using Python's `abc` module, create an abstract `PaymentMethod` class with an abstract method `pay(amount)`. Create `CreditCard` and `CryptoWallet` subclasses implementing it differently. Attempting to instantiate `PaymentMethod` directly should raise a `TypeError`.

**Example:**
```
pm = PaymentMethod()
```
**Expected Output:**
```
TypeError: Can't instantiate abstract class PaymentMethod with abstract method pay
```

---

### 17. Custom Exception Hierarchy for a `Vending Machine`
Design a `VendingMachine` class along with custom exceptions `OutOfStockError` and `InsufficientFundsError` (both inheriting from a base `VendingMachineError`). The `purchase(item, money)` method should raise the appropriate exception depending on the situation.

**Example:**
```
vm = VendingMachine({"Coke": (2, 15)})  # (stock, price)
vm.purchase("Coke", 10)
```
**Expected Output:**
```
InsufficientFundsError: Need 5 more to buy Coke
```

---

### 18. Metaclasses: Enforcing Naming Conventions
Create a metaclass `UpperAttrMetaclass` that automatically converts all class attribute names to uppercase at class-creation time. Apply it to a class `Config` with lowercase attributes defined normally, and show the resulting attributes are uppercase.

**Example:**
```
class Config(metaclass=UpperAttrMetaclass):
    debug = True
    version = "1.0"

print(Config.DEBUG)
print(Config.VERSION)
```
**Expected Output:**
```
True
1.0
```

---

### 19. The Singleton Pattern: `Logger`
Implement a `Logger` class using the Singleton design pattern (only one instance should ever exist, no matter how many times it's constructed). Verify by comparing object identity.

**Example:**
```
log1 = Logger()
log2 = Logger()
print(log1 is log2)
log1.log("System started")
print(log2.get_logs())
```
**Expected Output:**
```
True
['System started']
```

---

### 20. Observer Pattern: `WeatherStation`
Build a `WeatherStation` (the "subject") that maintains a list of `Display` observers. When `set_temperature()` is called on the station, all registered displays should automatically update and print the new value.

**Example:**
```
station = WeatherStation()
d1 = PhoneDisplay()
d2 = TVDisplay()
station.attach(d1)
station.attach(d2)
station.set_temperature(28)
```
**Expected Output:**
```
Phone Display: Temperature updated to 28°C
TV Display: Temperature updated to 28°C
```

---

### 21. Operator Overloading + Custom Sorting: `Card` and `Deck`
Create a `Card` class (`suit`, `rank`) that implements `__lt__` and `__eq__` so cards can be compared and sorted by rank. Create a `Deck` class holding 52 `Card` objects, with a `sort_deck()` method that uses Python's built-in `sorted()`.

**Example:**
```
deck = Deck()
deck.shuffle()
deck.sort_deck()
print(deck.cards[0])
print(deck.cards[-1])
```
**Expected Output:**
```
2 of Clubs
Ace of Spades
```

---

### 22. Descriptors: Type-Enforced Attributes
Create a custom descriptor class `TypedProperty` that enforces a specific type for any attribute it manages. Use it inside a `Person` class so that assigning a non-integer to `age` raises a `TypeError`.

**Example:**
```
p = Person("Zanele", 25)
p.age = "old"
```
**Expected Output:**
```
TypeError: Expected <class 'int'>, got <class 'str'>
```

---

### 23. State Machine Pattern: `TrafficLight`
Implement a `TrafficLight` class using the State design pattern, where each state (`RedState`, `GreenState`, `YellowState`) is its own class implementing a `next()` transition, and the `TrafficLight` delegates to its current state object.

**Example:**
```
light = TrafficLight()
print(light.current_state())
light.next()
print(light.current_state())
light.next()
print(light.current_state())
```
**Expected Output:**
```
Red
Green
Yellow
```

---

### 24. Multiple Inheritance and MRO: Diamond Problem
Create four classes: `A` (base, with a method `greet()` returning `"A"`), `B` and `C` (both inherit from `A`, each overriding `greet()`), and `D` (inherits from both `B` and `C`). Call `D().greet()` and explain which method executes based on Python's Method Resolution Order (MRO). Print `D.__mro__` as well.

**Example:**
```
print(D().greet())
print([cls.__name__ for cls in D.__mro__])
```
**Expected Output:**
```
B
['D', 'B', 'C', 'A', 'object']
```

---

### 25. Custom Context Manager: `DatabaseConnection`
Create a `DatabaseConnection` class implementing `__enter__` and `__exit__` so it can be used with a `with` statement. It should print connection/disconnection messages, and safely close the connection even if an exception occurs inside the `with` block.

**Example:**
```
with DatabaseConnection("mydb") as db:
    db.query("SELECT * FROM users")
    raise ValueError("Bad query")
```
**Expected Output:**
```
Connecting to mydb...
Running query: SELECT * FROM users
Closing connection to mydb...
ValueError: Bad query
```

---

### 26. Composite Pattern: File System Tree
Build a `FileSystemItem` structure using the Composite pattern: a `File` class (leaf, has a size) and a `Folder` class (composite, can contain `Files` and other `Folders`). Both should implement a `total_size()` method so calling it on a `Folder` recursively sums everything inside it.

**Example:**
```
root = Folder("root")
root.add(File("a.txt", 100))
sub = Folder("sub")
sub.add(File("b.txt", 200))
root.add(sub)
print(root.total_size())
```
**Expected Output:**
```
300
```

---

### 27. Factory Pattern: `ShapeFactory`
Create a `ShapeFactory` class with a static/class method `create_shape(shape_type, **kwargs)` that returns the correct `Shape` subclass instance (`Circle`, `Square`, `Triangle`) based on a string input, without the caller needing to know the class names directly. Invalid types should raise a `ValueError`.

**Example:**
```
s = ShapeFactory.create_shape("circle", radius=4)
print(type(s).__name__)
print(round(s.area(), 2))
ShapeFactory.create_shape("hexagon")
```
**Expected Output:**
```
Circle
50.27
ValueError: Unknown shape type: hexagon
```

---

### 28. `__slots__` and Memory-Constrained Classes
Create a `Point3D` class using `__slots__` to restrict it to only `x`, `y`, `z` attributes (no dynamic attribute creation, no `__dict__`). Show that attempting to add a new attribute raises an `AttributeError`.

**Example:**
```
p = Point3D(1, 2, 3)
p.w = 4
```
**Expected Output:**
```
AttributeError: 'Point3D' object has no attribute 'w'
```

---

### 29. Chain of Responsibility: Support Ticket Escalation
Model a customer support system using the Chain of Responsibility pattern. Create `Level1Support`, `Level2Support`, and `Level3Support` handler classes, each with a `severity_threshold`. A ticket should be passed along the chain until a handler with sufficient authority resolves it, otherwise it passes to the next.

**Example:**
```
chain = Level1Support(Level2Support(Level3Support(None)))
chain.handle(Ticket("Server down", severity=9))
```
**Expected Output:**
```
Level1 cannot handle severity 9, passing up...
Level2 cannot handle severity 9, passing up...
Level3 is resolving ticket: Server down
```

---

### 30. Full System Design: `Library Management System` with Multiple OOP Pillars
Design a mini library management system combining everything: an abstract `LibraryItem` base class (`Book`, `DVD`, `Magazine` subclasses using inheritance and polymorphism), a `Member` class with encapsulated borrowing limits, a `Library` class managing checkouts/returns with custom exceptions (`ItemUnavailableError`, `BorrowLimitExceededError`), and operator overloading so two `Member` objects can be compared by number of books borrowed (`__lt__`).

**Example:**
```
lib = Library()
lib.add_item(Book("1984", "Orwell"))
member = Member("Naledi", borrow_limit=1)
lib.checkout(member, "1984")
lib.checkout(member, "1984")  # Already checked out
```
**Expected Output:**
```
'1984' checked out to Naledi.
ItemUnavailableError: '1984' is already checked out.
```

---

## How to Use This List
- Work through each challenge in a fresh `.py` file.
- Test your class against the sample input/output before considering it done.
- For the advanced section especially, try to identify *which design pattern or OOP pillar* each challenge is really testing (encapsulation, polymorphism, composition, etc.) — that's the real skill being built.

Good luck! 🐍
