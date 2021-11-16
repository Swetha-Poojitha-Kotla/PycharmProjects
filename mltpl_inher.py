#for examples.. initi method is having in all classes and c is child class of A and B..and then if e call super.initi method then it ill go from left to right..so left side (A,B) A class is there so it ill come from A



class A:
    def feature1(self):
        print("Feature 1...!!!")

    def feature2(self):
        print("Feature 2...!!!")


class B:
    def feature3(self):
        print("Feature 3...!!!")

    def feature4(self):
        print("Feature 4...!!!")


class C(A,B):
    def feature5(self):
        print("Feature 5...!!!")

    def feature6(self):
        print("Feature 6...!!!")


a1 = A()
b1 = B()
c1 = C()
c1.feature3()
b1.feature3()



