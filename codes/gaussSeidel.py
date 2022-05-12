from prettytable import PrettyTable

def gaussSeidel(x, y, z, accuracy):
    def f_x(x, y, z):
        f_x = (1 + y)/2
        return f_x

    def f_y(x, y, z):
        f_y = (8 + x + z)/3
        return f_y

    def f_z(x, y, z):
        f_z = (y - 5)/2
        return f_z


    n = 0
    table = PrettyTable(["No.", "x", "y", "z"])
    table.add_row([0, x, y, z])

    while True:
        old_x = x
        old_y = y
        old_z = z
        x = round(f_x(old_x, old_y, old_z), accuracy + 1)
        y = round(f_y(x, old_y, old_z), accuracy + 1)
        z = round(f_z(x, y, old_z), accuracy + 1)
        n = n + 1

        table.add_row([n, x, y, z])

        if(old_x == x and old_y == y and old_z == z):
            break

    print(table)
    print(f"The required solutions are {x}, {y} and {z} after {n} iterations.")



accuracy = int(input("Enter the accuracy of the decimal digits: ")) 

initial_x = float(input("Enter the initial approximation of x: "))
initial_y = float(input("Enter the initial approximation of y: "))
initial_z = float(input("Enter the initial approximation of z: "))

gaussSeidel(initial_x, initial_y, initial_z, accuracy)


