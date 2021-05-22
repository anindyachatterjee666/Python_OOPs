# constructors & alternative constructor and static method

class Employee:

    no_of_leaves = 10

    def __init__(self, name, roll, salary):
        self.name = name
        self.roll = roll
        self.salary = salary

    def printdetails(self):
        return f"The name is {self.name}, roll is {self.roll}, salary is {self.salary}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def frm_str(cls, str):
         # x = str.split("-")
         # return cls(x[0], x[1], x[2])
         return cls(*str.split(","))

    @staticmethod
    def gdprint(string):
        return f"{string} is a good boy."


# Employee.no_of_leaves = 22
# Employee.change_leaves(100)
# print(Employee.no_of_leaves)


harry = Employee("Harry", "12", "24500")
rohan = Employee("Rohan", "23", "35600")
gaurav = Employee.frm_str("Gourav, 54, 24700")

# print(gaurav.salary)

print(Employee.gdprint("Anindya"))