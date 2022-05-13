import numpy as np
from sympy import *

def backwardInterpolate(n, accuracy):
    x = np.zeros((n))
    y = np.zeros((n, n))

    for i in range (n):
        x[i] = float(input('Enter the value of x['+str(i)+']: '))
        y[i][0] = float(input('Enter the value of y['+str(i)+']: '))

    if all(np.round(np.diff(x), accuracy + 1) != np.round(np.diff(x)[0], accuracy + 1)):
        exit('The data points are not equally spaced.')

    
    print('Enter the value to interpolate:')
    value = round(float(input('x = ')), accuracy + 1)
    variable = symbols('x')

    h = round((x[n - 1] - x[0])/(n-1), accuracy + 1)
    p_x =((variable - x[n-1])/h)
    p = round((value - x[n-1])/h, accuracy + 1)

    for c in range(1, n):
        for r in range (0, n - c):
            y[r][c] = round(y[r + 1][c-1] - y[r][c-1], accuracy + 1)


    def getCoefficients(p, n):
            temp = p
            for i in range (1, n):
                temp = temp*(p+i)
            return temp

    def getFactorial(number):
        if(number == 0 or number == 1):
            return 1
        elif(number < 0):
            print ("Error.")
        else:
            return number * getFactorial(number - 1)

    solution_x = y[n-1][0]
    solution = y[n-1][0]

    for i in range(1, n):
        solution_x = (solution_x + (getCoefficients(p_x, i)*y[n-2][i]/getFactorial(i)))
        #print(round((getCoefficients(p, i)*y[n-i-1][i]/getFactorial(i)), accuracy + 1))
        solution = round(solution + (getCoefficients(p, i)*y[n-i-1][i]/getFactorial(i)), accuracy + 1)

    print('Equation = ', simplify(solution_x))
    print(f"Solution = {solution}")



accuracy = int(input("Enter the accuracy of the decimal digits: "))
n = int(input("Enter the number of data points: "))
backwardInterpolate(n, accuracy)

