# class UpperAttrMetaclass(type):
#     def __new__(mcs, name, bases, dict):
#         new_dict = {}
#         for k,v in dict.items():
#             if k.startswith("__"):
#                 new_dict[k] = v
#             else:
#                 new_dict[k.upper()] = v
#         return super().__new__(mcs, name, bases, new_dict)

# class Config(metaclass=UpperAttrMetaclass):
#     debug = True
#     version = "1.0"

# print(Config.DEBUG)
# print(Config.VERSION)