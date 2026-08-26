# Program 14: Print Multiplication Table of a Number
# Student: Nitish Kapoor (12625876)

n = 8

print(f"--- Multiplication Table of {n} ---")
for i in range(1, 11):
    print(f"{n} x {i:02d} = {n * i}")
