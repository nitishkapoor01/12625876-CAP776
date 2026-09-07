# Program 26: Sum of Digits & Divisibility Analysis
# Student: Nitish Kapoor (12625876)

num = 4536
temp = num
digit_sum = 0

while temp > 0:
    digit_sum += temp % 10
    temp //= 10

print(f"Number: {num} | Sum of Digits: {digit_sum}")
print(f"Even/Odd       : {'Even' if digit_sum % 2 == 0 else 'Odd'}")
print(f"Divisible by 3 : {digit_sum % 3 == 0}")
print(f"Divisible by 9 : {digit_sum % 9 == 0}")
