from sympy import *
from prettytable import PrettyTable
import math

def falsePostion(function, a, b, accuracy):
    def f(x):
        f = eval(function)
        return f

    n = 0

    tolerance = 0.5 / (10**(accuracy))
    print(f"The tolerance is {tolerance}.")

    table = PrettyTable(["No.", "a", "b", "x", "f(x)"])
   
    while true:
        f_a = f(a)
        function_a = round(f_a, accuracy + 1)
        f_b = f(b)
        function_b = round(f_b, accuracy + 1)

        i = ((a*function_b) - (b*function_a))/(function_b - function_a)
        x = round(i, accuracy + 1)
        f_x = f(x)
        function_x = round(f_x, accuracy + 1)
        n = n + 1

        table.add_row([n, a, b, x, function_x])
        if(abs(function_x) < tolerance):
            break

        elif(function_x * function_b < 0):
            a = x
        
        elif(function_x * function_a < 0):
            b = x

    print(table)
    print(f"The required root is {x} after {n} iterations.")


functionF = str(input("Enter the function f(x) for x: "))
accuracy = int(input("Enter the accuracy of the decimal digits: "))
a = float(input("Enter the first initial approximation of x: "))
b = float(input("Enter the final initial approximation of x: "))

x = symbols('x')

def f(x):
    f = eval(functionF)
    return f

if(f(a) * f(b) < 0):
    falsePostion(functionF, a, b, accuracy)
else:
    a = float(input("Re-enter the first initial approximation of x: "))
    b = float(input("Re-enter the final initial approximation of x: "))

        

        