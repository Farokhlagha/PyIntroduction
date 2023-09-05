# Write a function that prints a checkerboard 
# with dimensions n*m by receiving parameters n and m


n=int(input("enter number of rows:"))
m=int(input("enter number of coloumns:"))

def chess(n,m):
    for i in range(n):
        for j in range(m):
            if (i%2 + j%2)%2:
                print("* ",end=" ")
            else:
                print("# ",end=" ")
        print("")

chess(n,m)
