class A:
    def feature1(self):
        print("Feature 1...!!!")

    def feature2(self):
        print("Feature 2...!!!")


class B(A):
    def feature3(self):
        print("Feature 3...!!!")

    def feature4(self):
        print("Feature 4...!!!")


class C(B):
    def feature5(self):
        print("Feature 5...!!!")

    def feature6(self):
        print("Feature 6...!!!")


a1 = A()
b1 = B()
c1 = C()
a1.feature1()
a1.feature2()
b1.feature3()
b1.feature4()
b1.feature2()
c1.feature5()
c1.feature6()
c1.feature3()
c1.feature1()