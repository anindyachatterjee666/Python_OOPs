# Different types of Methods ( Instance Method , Class Method, Static Method)


''' Python program to show that the variables with a value assigned in class declaration, are class variables '''


# Class for Computer Science Student

class CSStudent:

    stream = 'cse'				 # Class Variable

    def __init__(self, name, roll):
        self.name = name		 # Instance Variable
        self.roll = roll		 # Instance Variable


# Objects of CSStudent class
a = CSStudent('Geek', 1)
b = CSStudent('Nerd', 2)


print(a.stream)     # prints "cse"
print(b.stream)     # prints "cse"
print(a.name)       # prints "Geek"
print(b.name)       # prints "Nerd"
print(a.roll)       # prints "1"
print(b.roll)       # prints "2"

# Class variables can be accessed using class name also

print(CSStudent.stream)     # prints "cse"

# Now if we change the stream for just a it won't be changed for b

a.stream = 'ME'
print(a.stream)     # prints 'ME'
print(b.stream)     # prints 'cse'

# To change the stream for all instances of the class we can change it directly from the class

CSStudent.stream = 'M.Tech'

print(a.stream) # prints 'M.Tech'
print(b.stream) # prints 'M.Tech'









# class student:
#
#     school = 'Telusko'                  # static or class variable
#
#     def __init__(self, m1, m2, m3):        # instance variables
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#
#     def avg(self):                      # instance method
#         return (self.m1 + self.m2 + self.m3)/3
#
#     @classmethod
#     def get_school(cls):                      # class method
#         return cls.school
#
#     @staticmethod                           # static method
#     def info():
#         return "Inside Static Method..."
#
#
# s1 = student(77, 65, 45)            # creating object of student
# s2 = student(44, 67, 97)
#
# print(s1.avg())                                 # printing instance methods
# print(student.get_school())                   # printing class method
# print(student.info())                           # printing static methods