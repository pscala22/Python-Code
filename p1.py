"""
Paul Scala
Z23561522
COP4045 - Python Programming
January 17, 2022
Homework #1
Problem #1
"""


import math
## This is obsolete: import pylab
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
        dis_value = b ** 2 - 4 * a * c
        sqrt_val = math.sqrt(abs(dis_value))

        if dis_value > 0:
            print ("Discriminant is greater than 0")
            print ("Two Solutions: ")
            x1 = ((-b + sqrt_val)/(2 * a))
            x2 = ((-b - sqrt_val)/(2 * a))
            print (x1, x2)

        elif dis_value == 0:
            print ("Discriminant is equal to 0")
            print ("One Solution")
            x =  (-b / (2 * a))
            print (x)

        elif dis_value < 0:
         print ("No Real Solutions") 

        else: 
            print ("Error")
    
        #Plotting Function  
        x = [i/10 for i in range(-30, 31)]
        y = [a * i ** 2 + b * i + c for i in x]
        if dis_value > 0:
            plt.xlim((min(x1,x2)-1, max(x1,x2)+1))
        else:
            plt.xlim((2*a-b-1, 2*a-b+1))
    plt.plot(x, y)
    plt.scatter(x, y)
    plt.show()