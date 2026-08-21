# Program 09: Check Whether a Number is Positive, Negative, or Zero
# Student: Nitish Kapoor (12625876)

test_numbers = [15, -8, 0, 42]

for n in test_numbers:
    if n > 0:
        print(f"Number {n} is Positive.")
    elif n < 0:
        print(f"Number {n} is Negative.")
    else:
        print("Number is Zero.")
