"""Khayyam Pascal's triangle is a sequence of numbers in
   which the value of each element is
   equal to the sum of the top value and the left top value. 
   By receiving the number n from the user; 
   Calculate Khayyam Pascal's triangle up to the nth line;
     Save in a two-dimensional array and then print."""

def KhayyamPascalsTriangle(n):
    KPT = []
    for i in range(n):
        KPT.append([0]*(i+2))
        KPT[i][0] = 1
        print(KPT[i][0] ,end="\t")
        for j in range(1,i+1):
            KPT[i][j] = KPT[i-1][j-1] + KPT[i-1][j]
            print(KPT[i][j] ,end="\t")
        print("")

KhayyamPascalsTriangle(4)