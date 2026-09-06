# Program 25: Reverse a Number and Check Palindrome
# Student: Nitish Kapoor (12625876)

num = 12321
temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = (rev * 10) + digit
    temp //= 10

print("Original Number:", num)
print("Reversed Number:", rev)
if num == rev:
    print(f"Result: {num} is a Palindrome Number.")
else:
    print(f"Result: {num} is NOT a Palindrome.")
