# By receiving two numbers from the user,
# the Greatest Common Factor (GCF) will calculate them.

number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))

for i in range(1, number1+1):
    if number1 % i == 0 and number2 % i == 0:
        GCF = i

print("bmm=", GCF)