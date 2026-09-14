# Program 33: Left and Right Aligned Star Triangles
# Student: Nitish Kapoor (12625876)

n = 5
print("Left-Aligned Triangle:")
for i in range(1, n + 1):
    print("*" * i)

print("\nRight-Aligned Triangle:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
