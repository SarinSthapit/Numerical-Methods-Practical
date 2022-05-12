
from sympy import *
from prettytable import PrettyTable
import math


def iterationmethod(function1, function2, x, y, accuracy):
#def iterationmethod(function1, function2, x, y, accuracy, max_Steps): => For second while loop. 
    
    def f(x, y):
        f = eval(function1)
        return f

    def g(x, y):
        g = eval(function2)
        return g
    
    i = None
    j = None
    n = 0
    old_x = None
    old_y = None

    tolerance = 0.5 / (10**(accuracy))
    print(f"The tolerance is {tolerance}.")

    table = PrettyTable(["No.", "x", "y"])
    table.add_row([0, x, y])
    while true:
    # while n < max_Steps: => The second while loop, for limited number of iterations.
    # This is useful when the maximum number of iterations are limited, such as in exams, when number of iterations have to be in a certain limit. The max_Steps  
    # paramater needs to be passed only when using this while loop.

        i = f(x, y)
        j = g(x, y)
        old_x = x
        old_y = y
        x = round(i, accuracy + 1)
        y = round(j, accuracy + 1)
        n += 1
        
        table.add_row([n, x, y])

        if(old_x == x and old_y == y):
            break

    print(table)
    print(f"The required root is {x} and {y} after {n} iterations.")
   




functionF = str(input("Enter the first function F(x, y) for x: "))
functionG = str(input("Enter the second function G(x, y) for y: "))
accuracy = int(input("Enter the accuracy of the decimal digits: ")) 
# max_Steps = int(input("Enter the maximum number of iterations: ")) => For the second while loop only.
initial_x = float(input("Enter the initial approximation of x: "))
initial_y = float(input("Enter the initial approximation of y: "))

x = symbols('x')
y = symbols('y')


# For the Convergence Test
derivativeF_wrt_x = str(diff(functionF, x)) # = ∂F/∂x
derivativeF_wrt_y = str(diff(functionF, y)) # = ∂F/∂y

derivativeG_wrt_x = str(diff(functionG, x)) # = ∂G/∂x
derivativeG_wrt_y = str(diff(functionG, y)) # = ∂G/∂y

def F_x(x, y):
    F_x = eval(derivativeF_wrt_x)
    return F_x

def G_x(x, y):
    G = eval(derivativeG_wrt_x)
    return G

def F_y(x, y):
    F_y = eval(derivativeF_wrt_y)
    return F_y

def G_y(x, y):
    G_y = eval(derivativeG_wrt_y)
    return G_y

a = F_x(initial_x, initial_y)
b = F_y(initial_x, initial_y)
c = G_x(initial_x, initial_y)
d = G_y(initial_x, initial_y)


# If both the functions satisfy the convergence test:
if((abs(a) + abs(b) < 1) and (abs(c) + abs(d) < 1)):
    iterationmethod(str(functionF), str(functionG), initial_x, initial_y, accuracy)
    # iterationmethod(str(functionF), str(functionG), initial_x, initial_y, accuracy, max_Steps) => For the second while loop only.

# If the function F(x, y) does not satisfy the convergence test:
elif((abs(a) + abs(b) > 1) and (abs(c) + abs(d) < 1)):
    print(f"The given function F(x, y) is not convergent.")
    # iterationmethod(str(functionF), str(functionG), initial_x, initial_y, accuracy) => To show the result even if F(x, y) is not convergent.
    # iterationmethod(str(functionF), str(functionG), initial_x, initial_y, accuracy, max_Steps) => For the second while loop only.

# If the functions G(x, y) does not satisfy the convergence test:
elif((abs(a) + abs(b) < 1) and (abs(c) + abs(d) > 1)):
    print(f"The given function G(x, y) is not convergent.")
    #  iterationmethod(str(functionF), str(functionG), initial_x, initial_y, accuracy) => To show the result even if G(x, y) is not convergent.
    # iterationmethod(str(functionF), str(functionG), initial_x, initial_y, accuracy, max_Steps) => For the second while loop only.

# If both the functions do not satisfy the convergence test:
else:
    print(f"The given functions F(x, y) and G(x, y) are not convergent.")
    # iterationmethod(str(functionF), str(functionG), initial_x, initial_y, accuracy) => To show the result even if F(x, y) and G(x, y) are not convergent.
    # iterationmethod(str(functionF), str(functionG), initial_x, initial_y, accuracy, max_Steps) => For the second while loop only.


# Questions for the presentation:

# x**2 + y = 11, x + y**2 = 7
# Function F(x, y): (11 - y) ** 0.5
# Function G(x, y): (7 - x) ** 0.5
# Initial approximations for x, y: 0, 0


# y**2 - 5y + 4 = 0, 3yx**2 -10 x + 7 = 0
# Function F(x, y): 0.1 * ((3*y*(x**2)) + 7)
# Function G(x, y): ((y**2) + 4)/5
# Initial approximations for x, y: 0.7, 0.8


# To run the code:
# cd "Sarin Sthapit_Roll No. 55_CE(II-II)_Double Iteration"
# python project.py