# function to subract two numbers
def subtract_numbers(a, b):
    try:
        # try to subtract b from a
        return a - b
    # TypeError checks that the inputs are the same type. So if a is an int and b is a string it will flag an error
    except TypeError: 
        # error handling
        return "Error: Both inputs must be numbers"

print(subtract_numbers(5, 2)) # should return 3
print(subtract_numbers(6, '9')) # should return "Error: Both inputs must be numbers"

# function to divide two numbers
def divide_numbers(a, b):
    # check if demoniator is 0
    if b == 0:
        # error handling
        return "Error: Cannot divide by zero"
    return a / b

print(divide_numbers(10, 2)) # should return 5
print(divide_numbers(11, 0)) # should return "Error: Cannot divide by zero"