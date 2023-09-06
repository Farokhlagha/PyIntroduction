# Receive the number n from the user. 
# Then draw a striped snake of length n. *#*#*#*#*#*#*#*#*#*#

n = int(input("enter your snake length: "))

for i in range(n):
    if i % 2 == 0:
        print("*", end="")

    else:
        print("#", end="")