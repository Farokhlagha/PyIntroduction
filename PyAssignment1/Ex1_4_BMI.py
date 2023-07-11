print("*** Welcome to Farokhlagha Calculation Body Mass Index (BMI) ***")

weight = float(input("enter your weight(Kg): "))
height = float(input("enter your height(m): "))

if weight <= 0 or height <= 0:
    print("Invalid input")
else:
    BMI = weight / height**2
    print(BMI)

    if BMI < 18.5:
        print("you are Underweight")
    elif 25 > BMI >= 18.5:
        print("you are in Normal Weight")
    elif 30 > BMI >= 25:
        print("you are Overweight")
    elif 35 > BMI >= 30 :
        print("you are Obecity")
    elif BMI >= 35:
        print("you are Extreme Obecity")