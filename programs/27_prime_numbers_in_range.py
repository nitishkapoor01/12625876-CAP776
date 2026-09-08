# Program 27: Print All Prime Numbers between 1 and N (No Functions)
# Student: Nitish Kapoor (12625876)

n = 50
print(f"Prime numbers between 1 and {n}:")

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
print()
