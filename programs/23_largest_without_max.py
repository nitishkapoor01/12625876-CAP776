# Program 23: Find Largest Number Without Using max()
# Student: Nitish Kapoor (12625876)

numbers = [45, 89, 12, 95, 34, 76, 23, 88, 19, 62]

largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print("Numbers:", numbers)
print("Largest Number (without max()):", largest)
