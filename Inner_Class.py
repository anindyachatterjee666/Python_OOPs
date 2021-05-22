# inner class


class student:

    def __init__(self, name, roll):      # instance variables
        self.name = name
        self.rollno = roll
        self.lap = self.laptop('Dell', 8, 'i5')      # creating obj of inner cls in the constructor of the outer cls

    def show(self):                 # instance method
        print(self.name, self.rollno)
        self.lap.show()         # calling the show() of the inner class from the outer class instance method

    class laptop:                   # inner class

        def __init__(self, brand, ram, cpu):    # inner class instance variables
            self.brand = brand
            self.ram = ram
            self.cpu = cpu

        def show(self):                         # printing the inner class values
            print(self.brand, self.ram, self.cpu)


s1 = student('Anindya', 10)                # creating obj of  outer class
s2 = student('Amit', 23)

s1.show()               # calling the instance method of outer class
print()
s2.show()

# print(s1.lap.brand)     # printing the inner class
# s1.lap.brand = 'Asus'   # changing the inner class variable from the outer class

# lap1 = s1.lap           # creating the inner class obj in outer class
# lap2 = s2.lap
#
# print(lap1.brand, lap1.cpu, lap1.ram)       # printing the inner class variables
# print(lap2.brand, lap2.cpu, lap2.ram)

# print(id(lap1))                       # showing the different addresses of different objects
# print(id(lap2))


# lap1 = student.laptop("Asus", 16, 'i9')   # creating the obj of inner class outside the outer class


''' You can create object of inner class inside the outer class(inside the constructor). 
                                or 
  you can create the object of inner class outside the outer class provided you use outer class name to call it '''


