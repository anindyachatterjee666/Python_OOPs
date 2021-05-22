# Exceptions

a = 6
b = 2

try:
    print("Resource open")
    print(a / b)
    k = int(input("Enter a Number:"))
    print(k)

except ZeroDivisionError as e:
    print("Invalid Input", e)

except ValueError as e:
    print("Invalid Input:", e)

except Exception as e:
    print("Something went wrong:", e)

finally:
    print("Resource closed")
