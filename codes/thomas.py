import numpy as np
from sympy import * 

def thomas(a, b, c, d, n):
    alpha = np.zeros((n))
    beta = np.zeros((n))
    x = np.zeros((n))

    alpha[0] = b[0]
    beta[0] = d[0]/b[0] 
    x[n - 1] = beta[n - 1]

    for i in range(1, n):
        alpha[i] = round(b[i] - ((a[i]*c[i - 1])/(alpha[i - 1])), accuracy + 1)
        print(alpha[i])


    for i in range(1, n):
        beta[i] = round((d[i] - (a[i]*beta[i - 1]))/alpha[i], accuracy + 1)
        print(beta[i])


    for i in range(n-2, -1, -1):
        if (i == n-2):
            x[i] = round(beta[i] - ((c[i]*beta[n-1])/(alpha[i])), accuracy + 1)
        elif(i == 0):
            x[i] = round(beta[i] - ((c[i]*x[i + 1])/(b[0])), accuracy + 1)
        else:
            x[i] = round(beta[i] - ((c[i]*x[i + 1])/(alpha[i])), accuracy + 1)
        print(x[i])



n = int(input("Enter the number of variables: "))
accuracy = int(input("Enter the accuracy of the decimal digits: "))
a = np.zeros((n))
b = np.zeros((n))
c = np.zeros((n))
d = np.zeros((n))

for i in range(0, n):
    a[i] = float(input('Enter the value of a['+str(i + 1)+']: '))

for i in range(0, n):
    b[i] = float(input('Enter the value of b['+str(i + 1)+']: '))

for i in range(0, n):
    c[i] = float(input('Enter the value of c['+str(i + 1)+']: '))

for i in range(0, n):
    d[i] = float(input('Enter the value of d['+str(i + 1)+']: '))

thomas(a, b, c, d, n)