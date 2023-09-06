# number is factorial?

number = int(input("please enter number: "))

couter = 0
Factorial = 1

while True:
    couter += 1
    Factorial *= couter
    if Factorial == number:
        print("yes")
        print(f"{couter}")
        break

    elif Factorial > number:
        print("no")
        break