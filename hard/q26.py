from abc import ABC, abstractmethod

# class FileSystemComponent(ABC):
#     @abstractmethod
#     def total_size(self):
#         pass

# class Folder(FileSystemComponent):
#     CHILDREN = []
#     size = 0
#     def __init__(self, name:str):
#         self.name = name

#     def add(self, sys_comp:FileSystemComponent):
#         self.size += sys_comp.total_size()
#         self.CHILDREN.append(sys_comp)

#     def total_size(self):
#         return self.size

# class File(FileSystemComponent):
#     def __init__(self, name:str, size:float):
#         self.name = name
#         self.size = size

#     def total_size(self):
#         return self.size

# root = Folder("root")
# root.add(File("a.txt", 100))
# sub = Folder("sub")
# sub.add(File("b.txt", 200))
# root.add(sub)
# print(root.total_size())