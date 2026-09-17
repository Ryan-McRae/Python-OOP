
# # QUESTION 9    
# class SecureFile:
#     def __init__(self, content, password):
#         self.__content = content
#         self.__password = password

#     def read(self, password):
#         if password == self.__password:
#             return self.__content
#         return "Access Denied"
# f = SecureFile("secretdata", "1234")
# f.__password = "wrong"
# print(f.read("wrong"))
# print(f.read("1234"))
