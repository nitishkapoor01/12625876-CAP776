# Program 40: Find Second Largest Number (No sort/max)
# Student: Nitish Kapoor (12625876)

nums = [45, 89, 12, 95, 34, 76]

largest = float('-inf')
second_largest = float('-inf')

for n in nums:
    if n > largest:
        second_largest = largest
        largest = n
    elif n > second_largest and n != largest:
        second_largest = n

print("Numbers:", nums)
print("Largest:", largest)
print("Second Largest:", second_largest)
