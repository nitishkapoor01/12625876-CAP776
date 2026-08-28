# Program 16: Function to Find Factorial of a Number
# Student: Nitish Kapoor (12625876)

def find_factorial(n):
    if n < 0:
        return "Undefined for negative numbers"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("Factorial of 5 is:", find_factorial(5))
print("Factorial of 6 is:", find_factorial(6))
