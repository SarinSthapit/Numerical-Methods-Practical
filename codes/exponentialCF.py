import math

def linearCF(n, accuracy):
    sum_x = 0
    sum_X = 0
    sum_y = 0
    sum_Y = 0
    sum_X2 = 0
    sum_XY = 0
    for i in range(n):
       x = float(input(f"Enter the value of x: "))
       sum_x += round(x, accuracy + 1)

       X = round(math.log(x, 10), accuracy + 1)
       sum_X =  round(sum_X + X, accuracy + 1)

       X2 = round(X * X, accuracy + 1)
       sum_X2 += round(X2, accuracy + 1)

       y = float(input("Enter the value of y: "))
       sum_y = round(sum_y + y, accuracy + 1)
       Y = round(math.log(y, 10), accuracy + 1)
       sum_Y = round(sum_Y + Y, accuracy + 1)

       XY = round(X * Y, accuracy + 1)
       sum_XY = round(sum_XY + XY, accuracy + 1)

    print(sum_X, sum_Y, sum_X2, sum_XY)
    solve(sum_X, sum_Y, sum_X2, sum_XY, n, accuracy)
       


def solve(sum_X, sum_Y, sum_X2, sum_XY, n, accuracy):
    def f_A(A, b):
        f_A = (sum_Y - b*(sum_X))/n
        return f_A

    def f_b(A, b):
        f_b = (sum_XY - A*sum_X)/sum_X2
        return f_b

    A = 1
    b = 2
    while True:
        old_A = A
        old_b = b
        A = round(f_A(old_A, old_b), accuracy + 1)
        b = round(f_b(A, old_b), accuracy + 1)

        if(old_A == A and old_b == b):
            break


    a = round(10**A, accuracy + 1)
    print("The required equation is: ")
    print(f"Y = {a}x^{b}")



n = int(input("Enter the number of points: "))
accuracy = int(input("Enter the accuracy of the decimal digits: ")) 
linearCF(n, accuracy)