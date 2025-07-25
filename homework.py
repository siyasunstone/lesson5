import math

n = float(input("Enter a number: "))
if n >= 0:
    print("Square root is", math.sqrt(n))
else:
    print("Cannot find square root of a negative number.")