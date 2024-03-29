def linearCF(n, accuracy):
    sum_x = 0
    sum_y = 0
    sum_x_square = 0
    sum_xy = 0
    for i in range(n):
       x = float(input(f"Enter the value of x: "))
       sum_x += round(x, accuracy + 1)
       x_square = round(x * x, accuracy + 1)
       sum_x_square += round(x_square, accuracy + 1)

       y = float(input("Enter the value of y: "))
       sum_y = round(sum_y + y, accuracy + 1)

       xy = round(x * y, accuracy + 1)
       sum_xy += round(xy, accuracy + 1)

    solve(sum_x, sum_y, sum_x_square, sum_xy, n, accuracy)
       


def solve(sum_x, sum_y, sum_x_square, sum_xy, n, accuracy):
    def f_a(a, b):
        f_a = (sum_y - b*(sum_x))/n
        return f_a

    def f_b(a, b):
        f_b = (sum_xy - a*sum_x)/sum_x_square
        return f_b

    a = 1
    b = 2
    while True:
        old_a = a
        old_b = b
        a = round(f_a(old_a, old_b), accuracy + 1)
        b = round(f_b(a, old_b), accuracy + 1)

        if(old_a == a and old_b == b):
            break
    
    print("The required equation is: ")
    print(f"Y = {a} + {b}x")



n = int(input("Enter the number of points: "))
accuracy = int(input("Enter the accuracy of the decimal digits: ")) 
linearCF(n, accuracy)