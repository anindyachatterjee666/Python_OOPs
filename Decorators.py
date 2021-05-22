# 1st
# def function1():
#     print("Subscribe now")
#
# fun2 = function1
#
# del function1
#
# fun2()


        # 2nd
#
# def funcret(num):
#     if num == 0:
#         return print
#     else:
#         return int
#
# print(funcret(0))




    # 3rd
#
# def execute(func):
#     print("Inside Execute")
#
# execute(sum)


            #4th

def dec1(fun1):
    def nowexe():
        print("Executing nowexe")
        fun1()
        print("Executed nowexe")
    return nowexe

@dec1
def who_is_harry():
    print("Harry is good boy")

# who_is_harry = dec1(who_is_harry)
who_is_harry()

