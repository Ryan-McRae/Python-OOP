
# QUESTION 11
# class Book:
#     def __init__(self, title:str):
#         self.title = title
#         self.is_checked_out = False

# class Library:
#     def __init__(self):
#         self.books:list[Book] = []

#     def add_book(self,book:Book):
#         self.books.append(book)

#     def checkout(self, title):
#         try:
#             for book in self.books:
#                 if book.title == title:
#                     book.is_checked_out = True
#         except Exception as e:
#             raise Exception from e

#     def return_book(self, title):
#         try:
#             for book in self.books:
#                 if book.title == title:
#                     book.is_checked_out = False
#         except Exception as e:
#             raise Exception from e

# lib = Library()
# lib.add_book(Book("Dune"))
# lib.checkout("Dune")
# print(lib.books[0].is_checked_out)
# lib.return_book("Dune")
# print(lib.books[0].is_checked_out)