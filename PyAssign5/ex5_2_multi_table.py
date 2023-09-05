# the multiplication table with dimensions n*m 
# after receiving parameters n and m

n=int(input("enter the first number:"))
m=int(input("enter the second number:"))      

def muliplication_table(n,m):

    for i in range(1, n+1):         
        for j in range(1, m+1):
            print(f'{i*j:3}', end=" ") 
        print(" ")  

muliplication_table(n,m)