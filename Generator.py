# Generator

        # top 10 perfect square

def topten():

    for i in range(1, 5):
        sq = i * i
        yield sq            # 'return' will terminate the programme but 'yield' doesn't .


value = topten()

print(type(value))          # <class 'generator'>

for j in value:
    print(j)