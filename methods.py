#instance methods -> Accessor methods (fetching)(get), mutator methods (change) (set)
#class methods
#static methods
#get info aout full class use "cls"
class Student:
    school = 'Andhra University College of Engineering'
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1 = value

#if not given, ill thro error...@decorator
    @classmethod
    def get_school(cls):
        return cls.school
#this static mthod has nthg to do it class methods or class variables or instance class or variables
#ant to perform any action ithout using any of this class things but ith other classes
    @staticmethod
    def get_info():
        print("This is Student class in xyz module")

s1 = Student(90,92,78);
s2 = Student(80,82,97);

print(s1.avg())
print(s2.avg())
print(Student.get_school())
Student.get_info()