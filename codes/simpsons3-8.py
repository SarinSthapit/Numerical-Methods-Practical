from prettytable import PrettyTable

def simpsons3_8(initial_x, final_x, n, accuracy):
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

        elif(i % 3 == 0):
            sum = round(sum + (2*y), accuracy + 1)

        elif(i % 3 != 0 and i > 0 and i < n):
            sum = round(sum + (3*y), accuracy + 1)

        else:
            print("It is out of range.")



    solution = round((3*h/8) * sum, accuracy + 1)
    print(f"The required solution is {solution}.")


initial_x = float(input("Enter the initial value of x: "))
final_x = float(input("Enter the final value of x: "))
n = int(input("Enter the number of subintervals: "))
accuracy = int(input("Enter the accuracy of the decimal digits: ")) 

if(n%3 == 0):
    simpsons3_8(initial_x, final_x, n, accuracy)
else:
    print("The number of subintervals in Simpson's 3/8 Rule must be even.")
