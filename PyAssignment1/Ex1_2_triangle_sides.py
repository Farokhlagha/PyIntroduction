import math

print("*** Welcome to FarokhLagha validation of the size of triangle sides ***")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a <= 0 or b <= 0 or c <= 0:
    print("invalid input")
else:
    
    if a + b > c and a + c > b and b + c > a:
        print("Congratulations; it's possible to draw a triangle with this dimensions")
    else:
        print("It's not possible to draw a triangle with this dimensions")