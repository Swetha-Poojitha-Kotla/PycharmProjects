class Computer:
    def __init__(self):
        self.name = 'poojitha'
        self.age = '24'
    def update(self):
        self.age = '25'
    def compare(self,other):
        if(self.age==other.age):
            return True;
        else:
            return False

#objects ill be in heap memory
#size of memory depends upon no of variables in class
#Constructor allocates size to object
# here computer is cons and it ill cal init method
c1 = Computer()
c2 = Computer()

if c1.compare(c2):
    print("They are same")

c1.name = 'Abhishek'
print(c1.name)
print(c2.name)

#as e are calling from c1 it ill consider c1 as self
c1.update()
print(c1.age)
print(c1.name)


