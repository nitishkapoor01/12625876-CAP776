# Program 17: Function to Check Prime Number
# Student: Nitish Kapoor (12625876)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for val in [11, 15, 23, 35, 47]:
    print(f"Number {val} -> Prime: {is_prime(val)}")
