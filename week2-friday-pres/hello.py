def subtract_numbers(a, b):
    try:
        return a - b
    except TypeError:
        return "Error: Both inputs must be numbers"

print(subtract_numbers(5, 2))
print(subtract_numbers(6, '9'))

def divide_numbers(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print(divide_numbers(10, 2))
print(divide_numbers(11, 0))