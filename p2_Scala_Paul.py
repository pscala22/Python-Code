"""
Paul Scala
Z23561522
COP4045 - Python Programming
January 17, 2022
Homework #1
Problem #2
"""

import math
## This is obsolete: import pylab
import matplotlib.pyplot as plt

#2 Pythagorean Numbers
print ("Problem 2: Pythagorean Numbers")

def find_Pythagorean(n):
# Checks to make sure each individual value is between 1 and n
# Keeping the starting initial range at 1 so no tuples are omitted
    for a in range (1, n+1):
        for b in range (1, n+1):
            for c in range (1, n+1):
# Runs each possibility within the range to validate that it is actually a tuple
                if (a**2+b**2==c**2):
# If tuple is validated, prints out the validated tuple
                    print("(",a,",",b,",",c,")")


#main function
n = int(input("Enter value of n: "))
print("Pythagorean Triplets: "), find_Pythagorean(n)
