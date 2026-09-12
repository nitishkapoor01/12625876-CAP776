# Program 31: Number Pyramid Pattern
# Student: Nitish Kapoor (12625876)

n = 5
print("Forward Pattern:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("\nReverse Pattern:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
