"""
# Discussion Assignment

Welcome to the Unit 2 Discussion Forum.

Write your own Python code examples that demonstrate each of the following. Do not copy examples from the book or any other source. Try to be creative with your examples to demonstrate that you invented them yourself.

The code and its output must be explained technically whenever asked. The explanation can be provided before or after the code, or in the form of code comments within the code. For any descriptive type question, your answer must be at least 150 words.

End your discussion post with one question related to programming fundamentals learned in this unit from which your colleagues can formulate a response or generate further discussion. Remember to post your initial response as early as possible, preferably by Sunday evening, to allow time for you and your classmates to have a discussion. Reply to two (2) of your classmates' posts.
"""


## Example 1: Define a function that takes an argument. Call the function. Identify what code is the argument and what code is the parameter.

def one_arg_func(arg): # arg is the parameter
    print(arg) # arg is the argument of the print function

one_arg_func("Hello, World!") # "Hello, World!" is the argument
# > Hello, World!

# Explanation:

# The function `one_arg_func` takes one parameter called `arg` and prints it. As the function is executed with the argument "Hello, World!", it will print "Hello, World!" to the console.

## Example 2: Call your function from Example 1 three times with different kinds of arguments: a value, a variable, and an expression. Identify which kind of argument is which.

one_arg_func(42) # 42 is a value
# > 42

my_var = "Hello, World!" # my_var is a variable
one_arg_func(my_var)
# > Hello, World!

one_arg_func(2 + 2) # 2 + 2 is an expression
# > 4

#Explanation:

# `one_arg_func` is executed with the value 42 as an argument, printing it to the console. `one_arg_func` is executed with the variable `my_var` as an argument, printing the value of `my_var` to the console. `one_arg_func` is executed with the expression 2 + 2 as an argument, printing the result of the expression to the console.

## Example 3: Construct a function with a local variable. Show what happens when you try to use that variable outside the function. Explain the results.

def local_var_func():
    local_var = "I am a local variable."
    print(local_var)

local_var_func()
# > I am a local variable.

# print(local_var) # This will raise a NameError because local_var is not defined outside the function
# > NameError: name 'local_var' is not defined

# Explanation:

# The function `local_var_func` defines a local variable `local_var` and prints it. When the function is executed, it prints the value of `local_var` to the console. When `local_var` is referenced outside the function, a NameError is raised because `local_var` is not defined in the global scope.

## Example 4: Construct a function that takes an argument. Give the function parameter a unique name. Show what happens when you try to use that parameter name outside the function. Explain the results.

def unique_param_func(unique_param):
    print(unique_param)

unique_param_func("I am a unique parameter.")
# > I am a unique parameter.

# print(unique_param) # This will raise a NameError because unique_param is not defined outside the function
# > NameError: name 'unique_param' is not defined

# Explanation:

# The function `unique_param_func` takes a parameter called `unique_param` and prints it. When the function is executed with the argument "I am a unique parameter.", it prints the value of `unique_param` to the console. When `unique_param` is referenced outside the function, a NameError is raised because `unique_param` is not defined in the global scope.

## Example 5: Show what happens when a variable defined outside a function has the same name as a local variable inside a function. Explain what happens to the value of each variable as the program runs.

same_name = "I am a global variable."

def same_name_func():
    same_name = "I am a local variable." # The local variable same_name shadows the global variable same_name
    print(same_name)

same_name_func()
# > I am a local variable.

print(same_name) # The value of the global variable same_name is not changed by the local variable same_name
# > I am a global variable.

# Explanation:

# The global variable `same_name` is defined with the value "I am a global variable." The function `same_name_func` defines a local variable `same_name` with the value "I am a local variable." When the function is executed, it prints the value of the local variable `same_name` to the console. The global variable `same_name` retains its original value and is not affected by the local variable `same_name`.

# Question for the class:

# What operators can we apply to strings and why can't we use certain ones on them?