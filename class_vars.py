#namespace is area here u create and store objects/variable
#class namespace -> wheels -> defined for all objects
#instance namespace -> mil and com -> defined only for objects
#inside init -> it instance variable if not it ill be class variable
class Car:
    wheels = 4
    def __init__(self):
        self.mil = '10kmph'
        self.com = 'Jaguar'


c1 = Car()
c2= Car()

c1.mil = '20kmph'
print(c1.mil)
print(c2.mil)