"""
Paul Scala
Z23561522
COP4045 - Python Programming
January 17, 2022
Homework #1
"""


import math
## This is obsolete: import pylab
import matplotlib.pyplot as plt

#1 Quadratic Equation
print ("Problem 1: Quadratic Equation")

#Asking for user input
a = float(input('Enter "a" value = '))
b = float(input('Enter "b" value = '))
c = float(input('Enter "c" value = '))

#Discriminant Value
if a == 0:
        print ("Discriminant is equal to 0")
        print ("Error")
else:
    dis_value = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis_value))

    if dis_value > 0:
        print ("Discriminant is greater than 0")
        print ("Real and different roots ")
        print ((-b + sqrt_val)/(2 * a))
        print ((-b - sqrt_val)/(2 * a))

    elif dis_value == 0:
        print ("Discriminant is equal to 0")
        print ("Real with the same roots")
        print (-b / (2 * a))

    else:
        print ("Discriminant is Complex") 
        print (-b / (2 * a)), " + i"
        print (-b / (2 * a)), " - i"

"""
#2 Pythagorean Numbers
print ("Problem 2: Pythagorean Numbers")


#3 Duplicated Substrings
print ("Problem 3: Duplicated Substrings")


#4 Function Visualization
print ("Problem 4: Function Visualization")
"""