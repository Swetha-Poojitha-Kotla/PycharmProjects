#self is like "this" keyword
#init is a constructor
class Computer:

    def configs(self):
        print(self.cpu, self.ram)

    # init method called automatically
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram


com1 = Computer('i5','16GB')
com2 = Computer('Ryzen','8GB')
# print(type(com1))
# print(com1.configs())
# Computer.configs(com1)
# Computer.configs(com2)
com1.configs()
com2.configs()
a = 867
