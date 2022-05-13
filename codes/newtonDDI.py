import numpy as np
from sympy import *

def DDI(n, accuracy):
    x = np.zeros((n))
    y = np.zeros((n, n))

    for i in range (n):
        x[i] = float(input('Enter the value of x['+str(i)+']: '))
        y[i][0] = float(input('Enter the value of y['+str(i)+']: '))

    ''' if all(np.round(np.diff(x), accuracy + 1) != np.round(np.diff(x)[0], accuracy + 1)):
        exit('The data points are not equally spaced.')
 '''
    
    print('Enter the value to interpolate:')
    value = round(float(input('x = ')), accuracy + 1)
    variable = symbols('x')

    h = round((x[n - 1] - x[0])/(n-1), accuracy + 1)
    p_x =(( variable - x[0])/h)
    p = round(( value - x[0])/h, accuracy + 1)

    for c in range(1, n):
        for r in range (0, n - c):
            y[r][c] = round((y[r + 1][c-1] - y[r][c-1])/(x[r + c] - x[r]), accuracy + 1)


    def getCoefficients(val, n):
            temp = 1
            for i in range (1, n):
                temp = temp * (val - x[i - 1])
            return temp

    def getFactorial(number):
        if(number == 0 or number == 1):
            return 1
        elif(number < 0):
            print ("Error.")
        else:
            return number * getFactorial(number - 1)

    solution_x = y[0][0]
    solution = y[0][0]

    for i in range(1, n):
        ''' solution_x = (solution_x + (getCoefficients(variable, i)*y[0][i]/getFactorial(i))) '''
        print(round((getCoefficients(value, i)*y[0][i]/getFactorial(i)), accuracy + 1))
        solution = round(solution + (getCoefficients(value, i)*y[0][i]/getFactorial(i)), accuracy + 1)

    #print('Equation = ', simplify(solution_x))
    print(f"Solution = {solution}")



accuracy = int(input("Enter the accuracy of the decimal digits: "))
n = int(input("Enter the number of data points: "))
DDI(n, accuracy)

