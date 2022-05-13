import numpy as np
from sympy import * 
x, y, z = symbols('x y z')

def LUmethod(matrix, b, n, accuracy):

    upper = np.zeros((n, n))
    lower = np.zeros((n, n))
    

    for i in range(n):
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])

            upper[i][k] = matrix[i][k] - sum

        
        for k in range(i, n):
            if(i == k): 
                lower[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum+=(lower[k][j] * upper[j][i])

                lower[k][i] = float((matrix[k][i] - sum)/upper[i][i])

     # Displaying the result :
    for i in range(n):
 
        # Lower
        for j in range(n):
            print(lower[i][j], end="\t")
        print("", end="\t")
 
        # Upper
        for j in range(n):
            print(upper[i][j], end="\t")
        print("")

    y = np.zeros((n))
    for i in range(n):
        y[i] = 0
        y1 = b[i]
        for j in range(n):
            if(i != j):
                y1 = y1 - lower[i][j]*y[j]
                

        y[i] = y1 / lower[i][i]
        print (y[i])        

    x = np.zeros((n))
    for i in range(n-1, -1, -1):
        x[i] = 0
        x1 = y[i]
        for j in range(n-1, -1, -1):
            if(i != j):
                x1 = round(x1 - upper[i][j]*x[j], accuracy + 1)
                

        x[i] = round(x1 / upper[i][i], accuracy + 1)

    for i in range(n):    
        print (x[i])        


n = int(input("Enter the number of variables: "))
accuracy = int(input("Enter the accuracy of the decimal digits: "))
matrix = np.zeros((n, n))
b = np.zeros((n))
for i in range(n):
    b[i] = float(input("Enter the value of coefficient at RHS: "))
    for j in range(n):
        matrix[i][j] = float(input('Enter the value at ['+str(i)+']['+str(j)+']: '))

LUmethod(matrix, b, n, accuracy)