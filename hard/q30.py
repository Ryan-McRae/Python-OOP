from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @property
    @abstractmethod
    def title(self):
        pass
    @property
    @abstractmethod
    def author(self):
        pass
    @property
    @abstractmethod
    def checked_out(self):
        pass

class Book(LibraryItem):
    title = None
    checked_out = False
    author= None
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author

class DVD(LibraryItem):
    title = None
    checked_out = False
    author= None
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author

class Magazine(LibraryItem):
    title = None
    checked_out = False
    author= None
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author

class Member:
    def __init__(self, name:str, borrow_limit:int):
        self.name = name
        self.limit = borrow_limit

class ItemUnavailableError(BaseException):
    def __str__(self):
        return "checked out already"

class BorrowLimitExceededError(BaseException):
    def __str__(self):
        return "limit reached"

class Library:
    ITEMS:list[LibraryItem] = []

    def __init__(self):
        pass
    def add_item(self, item:LibraryItem):
        self.ITEMS.append(item)

    def checkout(self, member:Member, title:str):
        if member.limit == 0:
            raise BorrowLimitExceededError
        
        for item in self.ITEMS:
            if (item.title == title):
                if item.checked_out == False:
                    item.checked_out = True
                    print(f"{item.title} checked out to {member.name}.")
                    return
        raise ItemUnavailableError

lib = Library()
lib.add_item(Book("1984", "Orwell"))
lib.add_item(DVD("Sounds of Schaub","Redact"))
items = lib.ITEMS
member = Member("Naledi", borrow_limit=10)
lib.checkout(member, "1984")
lib.checkout(member, "Sounds of Schaub")
lib.checkout(member, "1984")