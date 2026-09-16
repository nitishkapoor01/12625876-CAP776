# Program 35: N x N Checkerboard Pattern (* and #)
# Student: Nitish Kapoor (12625876)

n = 6
print(f"{n}x{n} Checkerboard Pattern:")
for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()
