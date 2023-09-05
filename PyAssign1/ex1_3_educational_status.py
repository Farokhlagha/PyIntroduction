# Calculation of the GPA and
# the student's academic status

print("*** Welcome to Farokhlagha Calculation of educational status programme ***")

name = input("enter your name: ")
family = input("enter your family: ")

a = float(input("Enter first score: "))
b = float(input("Enter second score: "))
c = float(input("Enter third score: "))

d = (a + b + c)/3

if d >= 17:
    result = "great"
elif 17 > d >= 12:
    result = "normal"
elif d < 12:
    result = "fail"

    
print(name + " " + family + "'s GPA is " + result)