# Program 42: Decimal to Binary without bin()
# Student: Nitish Kapoor (12625876)

decimal_num = 29
temp = decimal_num
binary_str = ""

if temp == 0:
    binary_str = "0"
else:
    while temp > 0:
        remainder = temp % 2
        binary_str = str(remainder) + binary_str
        temp //= 2

print(f"Decimal {decimal_num} in Binary is: {binary_str}")
