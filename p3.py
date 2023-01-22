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

#3 Duplicated Substrings
print ("Problem 3: Duplicated Substrings")

def find_dup_str(s, n):
    for i in range(len(s)-n+1):
        substring = s[i:i+n]
        if s.count(substring) > 1:
            return substring
    return ""
    

def find_max_dup(s):
    result = ""
    for n in range(len(s), 0, -1):
        temp = find_dup_str(s, n)
        if temp:
            result = temp
            break
    return result

#main
while True:
    s = input("Enter a string: ")
    if not s:
        break
    n = int(input("Enter a number: "))
    print(("Dup_String "),(find_dup_str(s, n)))
    print(("Max_Dup_String"),(find_max_dup(s)))
