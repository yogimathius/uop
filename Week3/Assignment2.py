# Create a Python program that prompts the user to enter two numbers. 
def divide_two_numbers(num_one, num_two):
  #  Introduce a condition that raises a runtime error if the second number is zero. 
  if num_two == 0:
    #  Provide an error message that clearly indicates the cause of the error. 
    raise RuntimeError("Divide by 0 is not allowed!")
  #  Implement a division operation on the entered numbers. 
  return num_one / num_two


print(divide_two_numbers(1, 0))

"""
Output:
Traceback (most recent call last):
  File "main.py", line 17, in <module>
    print(divide_two_numbers(1, 0))
  File "main.py", line 8, in divide_two_numbers
    raise RuntimeError("Divide by 0 is not allowed!")
RuntimeError: Divide by 0 is not allowed!
"""

# Error handling is essential in expressions or conditions to prevent the program from crashing when unexpected situations occur. In the case of division by zero, the error handling mechanism allows the program to detect this specific error and handle it gracefully.

# If the division by zero error is not handled in a program, it can lead to a runtime error that crashes the program abruptly. This can result in a poor user experience, loss of data, and potential security vulnerabilities.

# When an error is raised after executing a program, it's important to examine the "Traceback", also called a stack trace, which usually gives reliable clues for the type of error that is happening and the affected lines of code. For this example we experience a RuntimeError, with the message "Divide by 0 is not allowed!". The error was raised on line 8 in main.py. Stack traces in python generally show the most relevant line of code closest to the bottom, and moves up the call stack, in sequence of the function calls that led to the error.

# *Hot trick: the output in the stack trace that identifies the lines of code affected can usually be `cmd + click`'d to open the specific file with the cursor directly on that line!!*

# To handle the division by zero error in Python programs, developers can use conditional statements to check if the divisor is zero before performing the division operation. 

# If the developer is aware of what potential errors a function may raise, it is possible to handle the exception / error that is raised in a `try - except` block. This allows the developer to catch and handle and exception, preventing the program from terminating abruptly.
