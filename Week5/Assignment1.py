"""
Write program to display your name and perform following operations on it: 
Display n characters from left. (Accept n as input from the user)
Count the number of vowels. 
Reverse it. 
"""

def main():
    name = input("Enter your name: ")
    n = int(input("Enter the number of characters to display from the left: "))
    print(name[:n])
    vowels = 'aeiouAEIOU'
    count = 0
    for char in name:
        if char in vowels:
            count += 1
    print("Number of vowels:", count)
    print("Reverse:", name[::-1])
main()

# 150 word explanation with APA references

"""
The program displays the name of the user and performs three operations on it: displays n characters from the left, counts the number of vowels, and reverses the name. 

The program first prompts the user to enter their name and the number of characters to display from the left. 

The program then displays the first n characters of the name. It then counts the number of vowels in the name by iterating through each character and checking if it is a vowel. 

The count of vowels is displayed. 

Finally, the program reverses the name using slicing and displays the reversed name. 

This program demonstrates string manipulation and basic string operations in Python.
"""