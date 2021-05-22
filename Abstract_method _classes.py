# Abstract Class and Methods in Python

from abc import ABC, abstractmethod


class Computer(ABC):

    @abstractmethod         # abstract class
    def process(self):
        pass


class Laptop(Computer):

    def process(self):      # definition of the abstract class in the child class
        print("It's running")


class Programmer:

    def work(self, lap1):
        print("Solving Bugs")
        lap1.board()


class whiteboard(Laptop):

    def board(self):
        print("It's writting")
        # lap2 = Laptop()
        # lap2.process()


# com = Computer()
# lap1 = Laptop()
# com.process()
# com.process()
# prog1 = Programmer()
white1 = whiteboard()
white1.process()
# prog1.work(lap1)
# prog1.work(white1)