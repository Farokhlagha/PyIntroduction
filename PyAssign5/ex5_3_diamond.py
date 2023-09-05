# a function that prints a rhombus of size n 
# after receiving the number n from the user

n= int(input("enter number of rows: "))

def Rhombus(n):
    for i in range(n*2-1):
        for j in range(n*2-1):
            if abs(j - (n-1)) <= (n-1 - abs(i - (n-1))):
                print("*",end="")
            else:
                print(" ",end="")
        print("")

Rhombus(n)