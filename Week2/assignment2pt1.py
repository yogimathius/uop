"""
Part 1
The circumference of a circle is calculated by 2πr, where π = 3.14159 (rounded to five decimal places). Write a function called print_circum that takes an argument for the circle’s radius and prints the circle's circumference. 

Call your print_circum function three times with different values for radius. 

Include the following in your part 1 submission: 

The code for your print_circum function.
A screenshot showing inputs and outputs to three calls of your print_circum.
The code and its output must be explained technically. The explanation can be provided before or after the code, or in the form of comments within the code. 

"""

pi = 3.14159
def print_circum(radius):
  circumference = 2 * pi * radius
  print("The circle's circumference is: ", circumference)

print_circum(43)
# > The circle's circumference is:  270.17674
print_circum(25)
# > The circle's circumference is:  157.0795
print_circum(62)
# > The circle's circumference is:  389.55716
