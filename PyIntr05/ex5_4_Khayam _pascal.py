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

KhayyamPascalsTriangle(8)

# other way **************************

def khayyam_pascal_triangle(rows):
    triangle = [[1]]
    
    for i in range(1, rows):
        row = [1]
        for j in range(1, i):
            # Calculate each element as the sum of the top value and the left top value
            element = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(element)
        row.append(1)
        triangle.append(row)
    
    return triangle
khayyam_pascal_triangle(8)

def print_khayyam_pascal_triangle(triangle):
    max_width = len(' '.join(map(str, triangle[-1])))  # Calculate the maximum width for formatting
    for row in triangle:
        formatted_row = ' '.join(map(str, row))
        print(formatted_row.center(max_width))

rows = int(input("Enter the number of rows for Khayyam Pascal's triangle: "))
triangle = khayyam_pascal_triangle(rows)
print_khayyam_pascal_triangle(triangle)




