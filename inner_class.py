class Student:

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)

    class Laptop:
        def __init__(self):
            self.brand = 'DELL'
            self.ram = '8GB'
            self.core = 'Intel'
            self.graphics = 'NVIDIA'

        def show(self):
            print(self.brand, self.ram, self.core, self.graphics)


s1 = Student('Abhishek', '01')
s2 = Student('Poojitha', '29')
# you can create object of inner class inside the object of outer class
# you can create object of inner class outside the outer class provied u use outer class name to call it
# laptop cass is belongs to another class
lap1 = s1.lap
lap2 = s2.lap
lap3 = Student.Laptop()
lap4 = Student.Laptop()
s1.show()
print(lap1.show())
