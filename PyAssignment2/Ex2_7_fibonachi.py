#A program that receives n and prints n elements of the Fibonacci sequence

import array
array.array('i')

number = int(input("enter your number:"))

if number == 1:
    print("1")
elif number == 2:
    print("1, 1")
elif number > 2:
    Fibonacci = array.array('i',(0 for i in range(0,number)))

    Fibonacci[0] = 1
    Fibonacci[1] = 1
    print("1, 1", end=", ")
    for i in range(2, number):
        Fibonacci[i] = Fibonacci[i - 1] + Fibonacci[i - 2]
        print(Fibonacci[i], end= ", ")

elif number<=0:
    print("Invalid input")





# n=int(input("please enter number of Fibonacci series: "))

# f= [1]

# if n==1:
#     print(f)
    
# elif n==2:
#     f.append(1)
#     print(f)
    
# elif n>2:
#     f.append(1)
#     for i in range(2,n):
#         fi=f[i-1]+f[i-2]
#         f.append(fi)
    
#     print(f)

# elif n<=0:
#     print("Invalid input")