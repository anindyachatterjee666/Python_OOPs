# Iterator


# nums = [1,2,3]
#
#  it = iter(nums) # calling the pre-defined function i.e. iter()
#  print(it.__next__())    # printing the value
#  print(next(it))         # Another type of printing
#
#
# for i in nums:
#     print(i)


            # creating own iterator

class Topten:

    def __init__(self):
        self.num = 1        # taking a counter as num

    def __iter__(self):     # iter() for creating own iterator
        return self

    def __next__(self):     # next() for creating own iterator

        if self.num <= 10:  # condition for printing 1st ten values
            val = self.num
            self.num += 1   # incrementing the counter
            return val      # returning the values

        else:
                raise StopIteration
                ''' if the 'if' condition goes beyond the condition we need to raise an Exception 
                . i.e. " raise StopIteration " . For loop has the power to use it internally '''

values = Topten()

# print(next(values))
# print(next(values))

for i in values:
    print(i , end=" ")







