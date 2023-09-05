# Receiving two numbers from the user,
# the least common multiple (LCM) will calculate them.

number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))

for i in range(1, number1+1):
    if number1 % i == 0 and number2 % i == 0:
        GCF = i

LCM = number1 * number2 / GCF
print("kmm=", LCM)