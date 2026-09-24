# Program 43: Strong Number Check (e.g. 145 = 1! + 4! + 5!)
# Student: Nitish Kapoor (12625876)

import math

def is_strong_number(n):
    return sum(math.factorial(int(d)) for d in str(n)) == n

test_vals = [145, 2, 40585, 120]
for v in test_vals:
    print(f"Number {v} -> Strong Number: {is_strong_number(v)}")
