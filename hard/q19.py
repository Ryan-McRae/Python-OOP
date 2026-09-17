# class Logger:
#     logs = []

#     _instance = None
#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __int__(self):
#         pass

#     def log(self,message:str):
#         self.logs.append(message)

#     def get_logs(self):
#         return self.logs

# log1 = Logger()
# log2 = Logger()
# print(log1 is log2)
# log1.log("System started")
# print(log2.get_logs())