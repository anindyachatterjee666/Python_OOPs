'''
Create a class State with the below attributes:
state_id of type Number
state_name of type String
affected_count of type Number
days_of_lockdown of type Number

Create the __init__ method which takes all parameters in the above sequence. The method should set the value of
attributes to parameter values .

Create a method inside the class with the name increase_lockdown. This method takes a Number value as argument which is
the number of weeks by which the lockdown period should be increased and increases the days_of_lockdown count
accordingly.
e.g. If the days_of_lockdown is 14 and the given number_of_weeks is 3, then the updated days_of_lockdown of the state
should be 35 and return the same.

Create another class Country with the below attributes:
country_name of type String
state_list of type List having State objects

Create the __init__ method which takes all parameters in the above sequence. The method should set the value of
attributes to parameter values inside the method.

Create another method inside the class with the name 'calculate_increase_in_lockdown_period'.

The method takes the increase in number of lockdown weeks as first argument and state_id as the second argument.
The method should find the respective state, whose state_id is given as in the argument, increment the days_of_lockdown
as per the given days and return the respective state object with the extended days_of_lockdown. If the state with given
state_id is not found , then the method returns None.
Note: In Python None means NULL Object , Accordingly default mail will display the message 'No state Exists '
If the number of weeks of lockdown extension is less than equals to zero , then return the object as it is, means there
would not be any changes to the days_of_lockdown. For more clarity on the above boundary validations, please refer the
default main function.

Note:
Use the method increase_lockdown defined in the State class to calculate the extended lockdown period of the states .

Sample Input (below) description:
The 1st input taken in the main section is the number of State objects to be added to the list of States.
The next set of inputs are the state_id, state_name, affected_count and days_of_lockdown for each state taken one after
other and is repeated for number of objects given in the first line of input. The last but one line of input refers the
state_id, whose days_of_lockdown needs to be extended with with given number of weeks , mentioned in the last line

Note:
Use the method increase_lockdown defined in the State class to calculate the extended lockdown period of the states .

Sample Input (below) description:
The 1st input taken in the main section is the number of State objects to be added to the list of States.

The next set of inputs are the state_id, state_name, affected_count and days_of_lockdown for each state taken one after
other and is repeated for number of objects given in the first line of input

The last but one line of input refers the state_id, whose days_of_lockdown needs to be extended with with given number
of weeks , mentioned in the last line

Sample Input:
4
100
Maharashtra
1500
21
101
Tamil Nadu
700
14
102
Delhi
500
14
103
Karnataka
700
14
102
3

Output:
Delhi 35

For more clarity on Input/Output and Input data processing, please refer to the main
section of code , You can use this section to test your code.
'''



                                        # not fully solved

import numpy


class State:  # creating class state

    print("Enter the State_id, State_name, affected_count, days_of_lockdown:")

    def __init__(self):  # constructor
        self.state_id = int(input())  # i/p int 101
        self.state_name = input()  # i/p string    'Delhi'
        self.affected_count = int(input())  # i/p number  500
        self.days_of_lockdown = int(input())  # i/p number    14

    def in_lkdn(self, no_week):  # creating increase lockdown method
        x = self.days_of_lockdown + 7 * no_week
        return x

    # def show(self):
    #     print(in_lkdn())
    #     print(self.state_id, self.state_name, self.affected_count, self.days_of_lockdown)


class Country(State):

    def __init__(self):  # constructor
        super().__init__()
        # self.c_name = input()        # i/p string
        # self.s_list = []    # i/p list

    # def show(self):
    #     print(self.state_id, self.state_name, self.affected_count, self.days_of_lockdown,self.c_name)

    def calculate_increase_in_lockdown_period(self, no_weeks, s_id):
        if s_id == self.state_id:  # comparing the state_id with the user given state_id
            print(self.state_name, self.in_lkdn(no_weeks))  # printing the output


def main():
    print("Enter the No of State:")
    no_st = int(input())  # Taking the Number of States from the user
    obj = list()
    for i in range(no_st):  # creating n no. of objects
        obj.append(Country())

    s_id = int(input())  # State code in Country class
    no_week = int(input())  # Extension of Lockdown in Country class

    for j in range(1, no_st + 1):      # calling the function from the objects that we have created

        calculate_increase_in_lockdown_period(no_week, s_id)

    # s2 = State()
    # s3 = State()
    # s4 = State()


if __name__ == "__main__":
    main()

