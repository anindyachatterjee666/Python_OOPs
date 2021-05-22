# property of inheritance

class A:

    def __init__(self):         # constructor of super class
        print("Inside init method of class A")

    def feature1(self):
        print("Featuer 1-A is working")

    def feature2(self):
        print("Featuer 2 is working")


class B:

    def __init__(self):            # constructor of sub class
        super().__init__()          # calling the super class constructor
        print("Inside init method of class B")

    def feature1(self):
        print("Featuer 1-B is working")

    def feature4(self):
        print("Featuer 4 is working")


class C(A, B):
    def __init__(self):
        super().__init__()          # calling super class constructor from child class
        print("Inside init method of class C")


a1 = C()
a1.feature1()

# a1.feature1()