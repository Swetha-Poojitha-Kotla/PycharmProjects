# method overloading -> same name but diff arguments
# method overriding -> same name same parameters but in diff classes and are inherited

class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, m1=None, m2=None, m3=None):
        s= 0
        if m1!=None and m2!=None and m3!=None:
            s = m1 + m2 + m3
        elif m1!=None and m2!=None:
            s = m1+m2
        else:
            s = m1

        return s


s1 = Student(54,78)
print(s1.sum(5, 6,6))
