def quadraticCF(n, accuracy):
    sum_x = 0
    sum_y = 0
    sum_x2 = 0
    sum_x3 = 0
    sum_x4 = 0
    sum_xy = 0
    sum_x2_y = 0
    for i in range(n):
       x = float(input(f"Enter the value of x: "))
       sum_x += round(x, accuracy + 1)
       x2 = round(x * x, accuracy + 1)
       x3 = round(x * x * x, accuracy + 1)
       x4 = round(x * x * x * x, accuracy + 1)

       sum_x2 += round(x2, accuracy + 1)
       sum_x3 += round(x3, accuracy + 1)
       sum_x4 += round(x4, accuracy + 1)

       y = float(input("Enter the value of y: "))
       sum_y = round(sum_y + y, accuracy + 1)

       xy = round(x * y, accuracy + 1)
       x2_y = round(x * x * y, accuracy + 1)

       sum_xy += round(xy, accuracy + 1)
       sum_x2_y += round(x2_y, accuracy + 1)

    solve(sum_x, sum_y, sum_x2, sum_x3, sum_x4, sum_xy, sum_x2_y, n, accuracy)
       


def solve(sum_x, sum_y, sum_x2, sum_x3, sum_x4, sum_xy, sum_x2_y, n, accuracy):
    def f_a(a, b, c):
        f_a = (sum_y - b*(sum_x) - c*(sum_x2))/n
        return f_a

    def f_b(a, b, c):
        f_b = (sum_xy - a*sum_x - c*sum_x3)/sum_x2
        return f_b

    def f_c(a, b, c):
        f_c = (sum_x2_y - a*sum_x2 - b*sum_x3)/sum_x4
        return f_c

    a = 1
    b = 1
    c = 1
    while True:
        old_a = a
        old_b = b
        old_c = c
        a = round(f_a(old_a, old_b, old_c), accuracy + 1)
        b = round(f_b(a, old_b, old_c), accuracy + 1)
        c = round(f_c(a, b, old_c), accuracy + 1)

        if(old_a == a and old_b == b and old_c == c):
            break
    
    print("The required equation is: ")
    print(f"Y = {a} + {b}x + {c}x^2")



n = int(input("Enter the number of points: "))
accuracy = int(input("Enter the accuracy of the decimal digits: ")) 
quadraticCF(n, accuracy)