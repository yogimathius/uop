"""
Q 1. The following is the countdown function copied from Section 5.8 of your textbook. 
 
def countdown(n): 
     if n <= 0: 
          print('Blastoff!') 
     else: 
          print(n) 
          countdown(n-1) 

Write a new recursive function countup that expects a negative argument and counts “up” from that number. Output from running the function should look something like this: 

>>> countup(-3) 
-3 
-2 
-1 
Blastoff! 

Write a Python program that gets a number using keyboard input. (Remember to use input for Python 3 but raw_input for Python 2.) 

If the number is positive, the program should call countdown. If the number is negative, the program should call countup. Choose for yourself which function to call (countdown or countup) for input of zero. 

Provide the following. 

The code of your program. 

Respective output for the following inputs: a positive number, a negative number, and zero. 

An explanation of your choice for what to call for input of zero. 
"""

def countup(n): 
    if n >= 0: 
        print('Blastoff!') 
    else: 
        print(n) 
        countup(n+1) 
 
def countdown(n): 
    if n <= 0: 
        print('Blastoff!') 
    else: 
        print(n) 
        countdown(n-1) 

def main():
    number = int(input("Enter a number: "))
    if number > 0:
        countdown(number)
    elif number < 0:
        countup(number)
    else:
        print('Blastoff!') 

main()

"""
Output:
Enter a number: 5 (countdown(5) is called)
5
4
3
2
1
Blastoff!
"""

"""
Output:
Enter a number: -3 (countup(-3) is called)
-3
-2
-1
Blastoff!
"""

"""
Output:
Enter a number: 0 (countdown(0) is called)
Blastoff!
"""

# Explanation: I chose to blastoff for input of zero without calling either functions, because the function countup is designed to count up from a negative number, and countdown is designed to count down from a positive number. Since zero is neither positive nor negative, it doesn't make sense to call either function. Instead, I chose to print "Blastoff!" directly for input of zero.