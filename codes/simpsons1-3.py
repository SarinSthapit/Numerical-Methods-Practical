from prettytable import PrettyTable

def simpsons1_3(initial_x, final_x, n, accuracy):
    def f(x):
        f = x**2 + 2.71828**x
        return f

    h = (final_x - initial_x)/n

    sum = 0
    
    for i in range(n + 1):
        x = initial_x + (i * h)
        y = round(f(x), accuracy + 1)
        
        if(i == 0 or i == n):
            sum = round(sum + y, accuracy + 1)

        elif(i % 2 == 0):
            sum = round(sum + (2*y), accuracy + 1)

        elif(i % 2 != 0 and i > 0 and i < n):
            sum = round(sum + (4*y), accuracy + 1)

        else:
            print("It is out of range.")



    solution = round((h/3) * sum, accuracy + 1)
    print(f"The required solution is {solution}.")


initial_x = float(input("Enter the initial value of x: "))
final_x = float(input("Enter the final value of x: "))
n = int(input("Enter the number of subintervals: "))
accuracy = int(input("Enter the accuracy of the decimal digits: ")) 

if(n%2 == 0):
    simpsons1_3(initial_x, final_x, n, accuracy)
else:
    print("The number of subintervals in Simpson's 1/3 Rule must be even.")
