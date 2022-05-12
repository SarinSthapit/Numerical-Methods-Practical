from prettytable import PrettyTable

def trapezoidalDouble(initial_x, final_x, initial_y, final_y, n, accuracy):
    def f(x, y):
        f = x**2 + 2.71828**y
        return f

    h = (final_x - initial_x)/n
    k = (final_y - initial_y)/n

    sum = 0
    
    for i in range(n + 1):
        x = initial_x + (i * h)
        for j in range(n + 1):
            y = initial_y + (j * k)
            value = round(f(x, y), accuracy + 1)
        
            if(i == 0 or i == n):
                if(j == 0 or j == n):
                    sum = round(sum + value, accuracy + 1)
                else:
                    sum = round(sum + 2*value, accuracy + 1)

            elif(i<6 and i>0):
                if(j == 0 or j == n):
                    sum = round(sum + 2*value, accuracy + 1)
                else:
                    sum = round(sum + 4*value, accuracy + 1)

            else:
                print("It is out of range.")


    solution = round((h * k/4) * sum, accuracy + 1)
    print(f"The required solution is {solution}.")


initial_x = float(input("Enter the initial value of x: "))
final_x = float(input("Enter the final value of x: "))
initial_y = float(input("Enter the initial value of y: "))
final_y = float(input("Enter the final value of y: "))
n = int(input("Enter the number of subintervals: "))
accuracy = int(input("Enter the accuracy of the decimal digits: ")) 

trapezoidalDouble(initial_x, final_x, initial_y, final_y, n, accuracy)
