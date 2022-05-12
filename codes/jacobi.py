from sympy import *
from prettytable import PrettyTable
import math

def jacobiMethod(function_x, function_y, function_z, x, y, z, accuracy):
    def f_x(x, y, z):
        f = eval(function_x)
        return f

    def f_y(x, y, z):
        f_y = eval(function_y)
        return f_y
    
    def f_z(x, y, z):
        f_z = eval(function_z)
        return f_z
    n = 0
    table = PrettyTable(["No.", "x", "y", "z"])
    table.add_row([0, x, y, z])

    while true:
        old_x = x
        old_y = y
        old_z = z
        x = round(f_x(old_x, old_y, old_z), accuracy + 1)
        y = round(f_y(old_x, old_y, old_z),  accuracy + 1)
        z = round(f_z(old_x, old_y, old_z),  accuracy + 1)
        n = n + 1

        table.add_row([n, x, y, z])

        if(old_x == x and old_y == y and old_z == z):
            break

    print(table)
    print(f"The required solutions are {x}, {y} and {z} after {n} iterations.")


function1 = str(input("Enter the first function f(x, y, z) for x: "))
function2 = str(input("Enter the second function f(x, y, z) for y: "))
function3 = str(input("Enter the third function f(x, y, z) for z: "))

accuracy = int(input("Enter the accuracy of the decimal digits: ")) 

initial_x = float(input("Enter the initial approximation of x: "))
initial_y = float(input("Enter the initial approximation of y: "))
initial_z = float(input("Enter the initial approximation of z: "))


jacobiMethod(function1, function2, function3, initial_x, initial_y, initial_z, accuracy)




