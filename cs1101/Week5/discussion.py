"""
For each function, describe what it actually does when called with a string argument. If it does not correctly check for lowercase letters, give an example argument that produces incorrect results, and describe why the result is incorrect.
"""

def any_lowercase1(s):
     for c in s:
          if c.islower():
               return True
          else:
               return False
          
# This function does not correctly check if any character in the string is lowercase. This function checks if the first character in the string is lowercase. If it is, it returns True. If it is not, it returns False. If the string is empty, the function will return None because the function doesn't return anything when the string is empty.

def any_lowercase2(s):
     for c in s:
          if 'c'.islower():
               return 'True'
          else:
               return 'False'
# This function does not correctly check if any character in the string is lowercase. This function checks if the character 'c' is lowercase. Since 'c' is always lowercase, the function will always return 'True'. If the string is empty, the function will return None because the function doesn't return anything when the string is empty. **This function also returns the string 'True' and 'False' instead of the boolean values True and False.**

def any_lowercase3(s):
     for c in s:
          flag = c.islower()
     return flag

# This function does not correctly check if any character in the string is lowercase. This function checks if the last character in the string is lowercase. If it is, it returns True. If it is not, it returns False. If the string is empty, the function will return an error because the variable flag is not associated with a value.

def any_lowercase4(s):
     if len(s) == 0:
          return False
     else
     return any(c.islower() for c in s)

    #  flag = False
    #  for c in s:
    #       flag = flag or c.islower()
    #  return flag

# This is the correct function that checks if any character in the string is lowercase. This function checks if any character in the string is lowercase. If it is, it returns True. If it is not, it returns False. If the string is empty, the function will return False.

def any_lowercase5(s):
     for c in s:
          if not c.islower():
               return False
     return True

# This function does not correctly check if any character in the string is lowercase. This function checks if all characters in the string are lowercase. If they are, it returns True. If they are not, it returns False. If the string is empty, the function will return True.

# # Test cases for any_lowercase1
# print("any_lowercase1") 
# print(any_lowercase1("Hello"))  # Expected: True, Actual: False
# print(any_lowercase1("HELLO"))  # Expected: False, Actual: False
# print(any_lowercase1("hello"))  # Expected: True, Actual: True
# print(any_lowercase1("HeLLo"))  # Expected: True, Actual: True
# print(any_lowercase1(""))       # Expected: False, Actual: False

# # Test cases for any_lowercase2
# print("any_lowercase2")  
# print(any_lowercase2("Hello"))  # Expected: True, Actual: 'True'
# print(any_lowercase2("HELLO"))  # Expected: False, Actual: 'True'
# print(any_lowercase2("hello"))  # Expected: True, Actual: 'True'
# print(any_lowercase2("HeLLo"))  # Expected: True, Actual: 'True'
# print(any_lowercase2(""))       # Expected: 'True', Actual: 'True'

# # Test cases for any_lowercase3
# print("any_lowercase3")  
# print(any_lowercase3("Hello"))  # Expected: True, Actual: True
# print(any_lowercase3("HELLO"))  # Expected: False, Actual: False
# print(any_lowercase3("hello"))  # Expected: True, Actual: True
# print(any_lowercase3("HeLLo"))  # Expected: True, Actual: True
# print(any_lowercase3(""))       # Expected: False, Actual: UnboundLocalError: cannot access local variable 'flag' where it is not associated with a value

# Test cases for any_lowercase4
print("any_lowercase4s")
print(any_lowercase4("Hello"))  # Expected: True, Actual: True
print(any_lowercase4("HELLO"))  # Expected: False, Actual: False
print(any_lowercase4("hello"))  # Expected: True, Actual: True
print(any_lowercase4("HeLLo"))  # Expected: True, Actual: True
print(any_lowercase4(""))       # Expected: False, Actual: False

# # Test cases for any_lowercase5
# print("any_lowercase5")
# print(any_lowercase5("Hello"))  # Expected: False, Actual: False
# print(any_lowercase5("HELLO"))  # Expected: False, Actual: False
# print(any_lowercase5("hello"))  # Expected: True, Actual: True
# print(any_lowercase5("HeLLo"))  # Expected: False, Actual: False
# print(any_lowercase5(""))       # Expected: True, Actual: True
