"""
Paul Scala
Z23561522
COP4045 - Python Programming
January 17, 2022
Homework #1
Problem #1
"""

import math
import matplotlib.pyplot as plt

#1 Quadratic Equation
print ("Problem 1: Quadratic Equation")
while True:
    #Asking for user input
    a = float(input('Enter "a" value = '))
    if not a:
        break
    b = float(input('Enter "b" value = '))
    c = float(input('Enter "c" value = '))

    #Discriminant Value
    if a != 0:
        dis_value = b ** 2 - 4 * a * c #calculating discriminant
        sqrt_val = math.sqrt(abs(dis_value))

        if dis_value > 0:
            x1 = ((-b + sqrt_val)/(2 * a))
            x2 = ((-b - sqrt_val)/(2 * a))
            print (("Two Solutions: x1="),("%.5f" % x1)," x2=","%.5f" % x2) #Printing solutions to 5 decimal places

        elif dis_value == 0:
            print ("Discriminant is equal to 0")
            print ("One Solution")
            x =  (-b / (2 * a))
            print (("One Solution: "),("%.5f" % x)) #Printing solution to 5 decimal places

        elif dis_value < 0:
         print ("No Real Solutions") 

        else: 
            print ("Error")
    
        #Plotting Function  
        x = [i/10 for i in range(-30, 31)] # 150 points
        y = [a * i**2 + b * i + c for i in x]
    if dis_value > 0:
        plt.xlim((min(x1, x2)-1, max(x1, x2)+1))
    else:
        plt.xlim((-b/a-1, -b/a+1))
    plt.ylim((min(y)-1, max(y)+1)) # adjust the y axis limit
    plt.plot(x, y)
    plt.scatter(x, y)
    plt.show()