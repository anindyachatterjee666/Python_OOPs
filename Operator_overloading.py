        # Operator Overloading

# b = 3
# a = 5
#
# print(a + b)
#
# print(int.__add__(a,b))

#
# a = '5'
# b = '30'
#
# print(str.__add__(a,b))



class Student:

    def __init__(self, m1, m2):     # initializing the instance variables
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):           # 's1' is going to 'self' and 's2' is going to 'other'
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)    # as we are passing 2 objs so we have to return the value through an obj i.e. s3 here

        return s3

    def __gt__(self, other):        # overloading __gt__() (gt = greater than)
        m1 = self.m1 + other.m1
        m2 = self.m1 + other.m2
        if m1 > m2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(20, 40)        # creating obj of student
s2 = Student(60, 33)

s3 = s1 + s2        # (inner calling) Student.__add__(s1, s2)

print(s3.m1)

if s1 > s2:             #
    print("S1 Wins")
else:
    print("S2 wins")


# a = 3
# print(a)        # printing the value of a

print(s2)       # printing the address of s1 object

# we want to print the value of s1 object so we need to overload  __str__()





