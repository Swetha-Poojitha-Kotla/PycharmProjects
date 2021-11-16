# pass means dont have anythng -> only declaration but not def -> abstract ethods and classes having are called abstract classes
# cannot create
# Can't instantiate abstract class Computer with abstract methods process
# Can't instantiate abstract class Laptop with abstract methods process
#child clss shud implement all the abstract methods from its abstract paretn class oter ise it ill become abstract class
#its used -> hen design any project
from abc import ABC, abstractmethod


class Computer(ABC):
    @abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("Its running")

class Programmer:
    def work(self,com):
        print("Solving problems")

class Board(Computer):
    def write(self):
        print("Its writing")

# c = Computer ()
l = Laptop()
l.process()
p = Programmer()

b= Board()
p.work(b)

