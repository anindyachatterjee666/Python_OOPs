#
#
# class computer:     # creating our own class
#
#     def config(self):       # method
#         print("i5 , 16 Gb , 1Tb")
#
# # a = 1
# com1.config()   # Another type of calling
# # print(type(a))
#
# com1 = computer()       # creating obj of our own class . com1 is the obj of class computer
# com2 = computer()
#
# # computer.config(com1)             # calling the methods of the class
# # computer.config(com2)
#
# com2.config()

#
# class computer:
#
#     def __init__(self, cpu, ram, hard):
#         self.cpu = cpu
#         self.ram = ram
#         self.hard = hard
#
#     def config(self):
#         print("Config is : ", self.cpu, self.ram, self.hard)
#
#
# comp1 = computer("Intel I5", 16, '2Tb')
# comp2 = computer("Ryzen 3200", 8, '3Tb')
#
# comp1.cpu = "I7 8400"
#
# comp1.config()
# print(type(comp1))



# class computer:
#
#     def __init__(self):
#         self.name = "Anindya"
#         self.age = 21
#
#     # def update(self):
#     #     self.age = 35
#
#     def compare(self,c2):
#         if self.age == c2.age:
#             return True
#         else:
#             return False
#
#
# c1 = computer()
# c1.age = 32
# c2 = computer()
#
#
# if c1.compare(c2):
#     print("They are same age:")
# else:
#     print("They are diff. age:")

# c1.update()
# c2.name = "Bitan"

# print(c1.name)
# print(c2.name)
# print(c1.age)
# print(c2.age)



class car:

    wheels = 4      # class variable

    def __init__(self):     # initialize the current class objects
        self.com = "BMW"
        self.mil = 10


c1 = car()      # creating object of class car
c2 = car()

c1.com = "AUDI"
c1.mil = 25
car.wheels = 5      # changing the value of static variable

print(c1.com, c1.mil, c1.wheels)   # Printing the values 
print(c2.com, c2.mil, c2.wheels)













