# Program 02: Swap Two Numbers
# Student: Nitish Kapoor (12625876)

a = 15
b = 30

print(f"Before Swapping: a = {a}, b = {b}")

# Method 1: Using arithmetic operations (without third variable)
a = a + b
b = a - b
a = a - b

print(f"After Swapping : a = {a}, b = {b}")
