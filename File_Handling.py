# file Concepts


# f1 = open('MyData_for_FileHandling', 'r')     # Opening the file in read mode
# f1.read()             # printing the data of the file

# f2 = open("Test2", 'w')         # opening another file in write mode
# f2.write("Anindya ")              # writing something in that file

# f2 = open("Test2", 'a')         # opening another file in append mode
# f2.write(" Chatterjee")          # adding data into the existing file

    # coping all the data from Mydata to Test2

# f1 = open("MyData_for_FileHandling", 'r')
# # print(type(f1))
# f2 = open("Test2", 'a')
# for data in f1:       # using loop for fetching values one by one
#     f2.write(data)


    # coping a image into another file

# f1 = open('Image.JPG', 'rb')        # rb = read in binary mode, for image we used this . f1 is the file we want to copy
# f2 = open('Timage.JPG', 'wb')       # pasting the image in f2 file in binary format
# for data in f1:
#     f2.write(data)


    # using with block

with open("MyData_for_FileHandling") as f:
    a = f.read()
    print(a)

f = open("MyData_for_FileHandling", 'r')
b = f.read()
print(b)