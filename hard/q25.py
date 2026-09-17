# class DatabaseConnection:
#     def __init__(self,database):
#         self.db = database

#     def __enter__(self):
#         print(f"Connecting to {self.db}...")
#         return self

#     def __exit__(self, exc_type, exc, tb):
#         print(f"Closign connection to {self.db}...")
#         return False

#     def query(self, q):
#         print(q)

# with DatabaseConnection("mydb") as db:
#     db.query("SELECT * FROM users")
#     raise ValueError("Bad query")