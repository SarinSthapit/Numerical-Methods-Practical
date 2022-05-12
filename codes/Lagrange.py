import numpy as np

def lagrange(n, accuracy, required_x):
    t = 1
    solution = 0

    x = np.zeros((n))
    y = np.zeros((n))
    
    for i in range(n):
       x[i] = float(input(f"Enter the value of x: "))
       y[i] = float(input("Enter the value of y: "))


    for j in range(n):
        term = 1
        for k in range(n):
            if( j != k): 
                term = round(term * (required_x - x[k])/(x[j] - x[k]), accuracy+1)
                
        print(term * y[j])
        solution = round( solution + (term * y[j]), accuracy + 1)

    print(f"The required solution is {solution}")


n = int(input("Enter the number of points: "))
accuracy = int(input("Enter the accuracy of the decimal digits: ")) 
required_x = float(input("Enter the point for which value is to be calculated, x: "))
lagrange(n, accuracy, required_x)
    


