from prettytable import PrettyTable

def rk4(x, y, n, final_x, accuracy):
    def f(x, y):
        f = y*(1 + x**2)
        return f

    h = round((final_x - x)/n, accuracy + 1)
    count = 0
    table = PrettyTable(["No.", "x", "y", "k1", "k2", "k3", "k4"])
    
    while True:
        old_y = y
        k1 = round(h * f(x, old_y), accuracy + 1)
        k2 = round(h*f(x+(h/2), y+(k1/2)), accuracy + 1)
        k3 = round(h*f(x+(h/2), y+(k2/2)), accuracy + 1)
        k4 = round(h * f(x + h, old_y + k3), accuracy + 1)
        y = round(old_y + ((1/6)*(k1 + 2*(k2 + k3) + k4)), accuracy + 1)
        count = count + 1

        x = round(x + h, accuracy + 1)
        table.add_row([count, x, y, k1, k2, k3, k4])
        if(x == final_x):
            break

        

    print(table)
    print(f"The required root is {y}")


accuracy = int(input("Enter the accuracy of the decimal digits: "))
initial_x = float(input("Enter the initial approximation of x: "))
final_x = float(input("Enter the final approximation of x: "))
initial_y = float(input("Enter the initial approximation of y: "))
n = int(input("Enter the number of subintervals:"))


rk4(initial_x, initial_y, n, final_x, accuracy)

