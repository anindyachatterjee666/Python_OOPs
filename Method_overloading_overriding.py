# Method Overloading, Method Overriding

''' Method overloading is not possible in Python directly we have to use some tricks here '''

# Method Overloading

# class Student:
#
#     def __init__(self, m1, m2):     # initializing the instance variables
#         self.m1 = m1
#         self.m2 = m2
#
#     def sum(self, a = None, b = None, c = None):
#         s = 0
#
#         if a != None and b != None and c != None:
#             s = a + b + c
#         elif a != None and b != None:
#             s = a + b
#         else:
#             s = a
#         return s
#
# s1 = Student(50, 50)
#
# x = s1.sum( )
#
# print(x)



# Method Overriding


class A:

    def show(self):
        print("Inside A show")

class B(A):

    def show(self):
        print("Inside B show")

a1 = B()

a1.show()

