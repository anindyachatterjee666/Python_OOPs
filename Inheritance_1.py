# inheritance

class A:

    def feature1(self):
        print("Featuer 1 is working")

    def feature2(self):
        print("Featuer 2 is working")


class B(A):     # iniheriting class A from B

    def feature3(self):
        print("Featuer 3 is working")

    def feature4(self):
        print("Featuer 4 is working")


class C(A,B):           # inheriting class A and b from C

    def feature5(self):
        print("Feature 5 is working")


a1 = A()
b1 = B()
c1 = C()

a1.feature3()
