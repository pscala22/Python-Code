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
def findDis (a,b,c):
    dis_value = b*b-4*a*c

    print("Discriminant value = ") + dis_value

    if dis_value > 0:
        print ("Discriminant is greater than 0")

    elif dis_value == 0:
        print ("Discriminant is equal to 0")

    elif dis_value < 0:
        print ("Discriminant is less than 0")

    else:
        print ("Unknown Error")

findDis(a,b,c)
"""
#2 Pythagorean Numbers
print ("Problem 2: Pythagorean Numbers")


#3 Duplicated Substrings
print ("Problem 3: Duplicated Substrings")


#4 Function Visualization
print ("Problem 4: Function Visualization")
"""