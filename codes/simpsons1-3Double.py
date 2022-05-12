from prettytable import PrettyTable

def simpsons1_3Double(initial_x, final_x, initial_y, final_y, n, accuracy):
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
                elif(j % 2 == 0):
                    sum = round(sum + 2*value, accuracy + 1)
                elif(j % 2 != 0 and j>0 and j<n):
                    sum = round(sum + 4*value, accuracy + 1)
                else:
                    print("It is out of range.")


            elif(i % 2 == 0):
                if(j == 0 or j == n):
                    sum = round(sum + 2*value, accuracy + 1)
                elif(j % 2 == 0):
                    sum = round(sum + 4*value, accuracy + 1)
                elif(j % 2 != 0 and j>0 and j<n):
                    sum = round(sum + 8*value, accuracy + 1)
                else:
                    print("It is out of range.")

            elif(i<n and i>0):
                if(j == 0 or j == n):
                    sum = round(sum + 4*value, accuracy + 1)
                elif(j % 2 == 0):
                    sum = round(sum + 8*value, accuracy + 1)
                elif(j % 2 != 0 and j>0 and j<n):
                    sum = round(sum + 16*value, accuracy + 1)
                else:
                    print("It is out of range.")

            else:
                print("It is out of range.")


    solution = round((h * k/9) * sum, accuracy + 1)
    print(f"The required solution is {solution}.")


initial_x = float(input("Enter the initial value of x: "))
final_x = float(input("Enter the final value of x: "))
initial_y = float(input("Enter the initial value of y: "))
final_y = float(input("Enter the final value of y: "))
n = int(input("Enter the number of subintervals: "))
accuracy = int(input("Enter the accuracy of the decimal digits: ")) 

if(n%2 == 0):
    simpsons1_3Double(initial_x, final_x, initial_y, final_y, n, accuracy)
else:
    print("The number of subintervals in Simpson's 1/3 Rule must be even.")
