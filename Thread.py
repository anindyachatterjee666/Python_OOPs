# Thread

from threading import *
from time import sleep


class Hello(Thread):        # Inheriting from Thread class

    def run(self):
        for i in range(5):
            print("Hallo")
            sleep(1)           # slowing down the scheduler for process execution


class Hi(Thread):                   # Inheriting from Thread class
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)                # slowing down the scheduler for process execution

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.5)                      # slow down the calling so there won't be any collision in the o/p
t2.start()

t1.join()
t2.join()
print("Bye")
