from sympy import *
import numpy as np

a = symbols('a')
b = symbols('b')
c = symbols('c')
x = symbols('x')
y = symbols('y')

def finiteDifference(initial_x, initial_y, final_x, final_y, n, accuracy):
    y2 = str(input("Enter the coeffiecient of y'': "))
    y1 = str(input("Enter the coeffiecient of y': "))
    y0 = str(input("Enter the coeffiecient of y: "))
    x0 = str(input("Enter the coeffiecient of x: "))


    variables_x = np.zeros((n))
    variables_y = [initial_y, a, b, c, final_y]
    h = (final_x - initial_x) / (n + 1)
    y_2 = [None] * (n + 1)
    y_1 = [None] * (n + 1)
    y_0 = [None] * (n + 1)
    x_0 = np.zeros((n + 1))
    equation = [None] * (n + 1)
    final_equation = [None] * (n + 1)
    matrix = np.zeros((n, n + 1))

    def f(x):
        f = eval(equation[i])
        return f

    def final(a, b, c):
        f = eval(str(final_equation[i + 1]))
        return f
    
    def fy2(x):
        fy2 = eval(y2)
        return fy2

    def fy1(x):
        fy1 = eval(y1)
        return fy1

    def fy0(x):
        fy0 = eval(y0)
        return fy0

    def fx0(x):
        fx0 = eval(x0)
        return fx0

   
    for i in range(1, 4):
        y_2[i] = (variables_y[i-1] - (2*(variables_y[i])) + variables_y[i + 1])/(h*h)
        y_1[i] = (variables_y[i + 1] - variables_y[i-1])/(2 * h)
        y_0[i] = variables_y[i]
        x_0[i] = round(initial_x + (i * h), accuracy + 1)

        equation[i] = str((fy2(x_0[i])*y_2[i]) + (fy1(x_0[i])*y_1[i]) + (fy0(x_0[i])*y_0[i]) - fx0(x_0[i]))
        final_equation[i] = simplify(f(x_0[i]))
        print(final_equation[i])


    for i in range(0, n):   
        for j in range(0, n + 1):
            if(j == n):
                temp = final(0,0,0)
                matrix[i][j] = -1 * float(temp)
                print(matrix[i][3])

            matrix[i][j] = final_equation[i + 1].coeff(variables_y[j + 1], 1)
            
    print(solve((final_equation[1], final_equation[2], final_equation[3]), (a, b, c)))
    

accuracy = int(input("Enter the accuracy of the decimal digits: "))
n = int(input("Enter the number of data points: "))

initial_x = float(input("Enter the initial approximation of x: "))
initial_y = float(input("Enter the initial approximation of y: "))
final_x = float(input("Enter the final approximation of x: "))
final_y = float(input("Enter the final approximation of x: "))

finiteDifference(initial_x, initial_y, final_x, final_y, n, accuracy)