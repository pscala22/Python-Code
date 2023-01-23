"""
Paul Scala
Z23561522
COP4045 - Python Programming
January 17, 2022
Homework #1
Problem #4
"""

import math
import matplotlib.pyplot as plt
import numpy as np

# 4 Function Visualization
print ("Problem 4: Function Visualization")

def plot_function(fun_str, domain, ns):
    xmin, xmax = domain
    xs = np.linspace(xmin, xmax, ns) # Create an array of x values that evenly divides the domain
    f = np.vectorize(lambda x: eval(fun_str)) # Create a vectorized version of the function
    ys = f(xs) # Apply the function to the x values to get the corresponding y values
    print("   x   |    y   ")
    print("-------|--------")
    for x, y in zip(xs, ys):
        print("{:+.3f} | {:+.3f}".format(x, y)) # Print a table of x and y values, adding a "+" sign to positive numbers
    plt.plot(xs, ys)
    plt.scatter(xs, ys) # Show the points on the graph
    plt.title(fun_str) # Set the title of the plot to the function string
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

 # main
fun_str = input("Enter a function in terms of x: ")
ns = int(input("Enter the number of samples: "))
xmin = float(input("Enter xmin: "))
xmax = float(input("Enter xmax: "))
plot_function(fun_str, (xmin, xmax), ns)