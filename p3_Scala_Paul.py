"""
Paul Scala
Z23561522
COP4045 - Python Programming
January 17, 2022
Homework #1
Problem #3
"""

import math
import matplotlib.pyplot as plt

#3 Duplicated Substrings
print ("Problem 3: Duplicated Substrings")

# Finds duplications within the string based on the "n" that the user initially inputs
def find_dup_str(s, n):
    for i in range(len(s)-n+1):
        substring = s[i:i+n] # Get a substring of length n
        if s.count(substring) > 1: # Check if the substring appears more than once in the original string
            return substring
    return ""
    
# Finds the largest duplication within the string
def find_max_dup(s):
    result = ""
    for n in range(len(s), 0, -1): # Iterate through the length of the string in reverse order
        temp = find_dup_str(s, n)
        if temp:
            result = temp
            break
    return result

# main
while True:
# If user types 'Enter' the program breaks
    s = input("Enter a string: ")
    if not s:
        break
    n = int(input("Enter a number: "))
    print(("Dup_String "),(find_dup_str(s, n)))
    print(("Max_Dup_String"),(find_max_dup(s)))