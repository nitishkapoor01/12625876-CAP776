# Program 32: 10x10 Multiplication Table Grid
# Student: Nitish Kapoor (12625876)

print("--- 10 x 10 MULTIPLICATION GRID ---")
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4d}", end="")
    print()
