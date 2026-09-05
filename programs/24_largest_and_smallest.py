# Program 24: Find Largest & Smallest without Built-ins
# Student: Nitish Kapoor (12625876)

nums = [35, 12, 78, 4, 99, 23, 56]
largest = nums[0]
smallest = nums[0]

for n in nums:
    if n > largest:
        largest = n
    if n < smallest:
        smallest = n

print("Numbers:", nums)
print("Smallest:", smallest)
print("Largest :", largest)
