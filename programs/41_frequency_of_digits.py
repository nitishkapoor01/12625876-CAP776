# Program 41: Frequency of Each Digit in a Number
# Student: Nitish Kapoor (12625876)

number_str = "112233445511"
frequency = {}

for digit in number_str:
    frequency[digit] = frequency.get(digit, 0) + 1

print(f"Number: {number_str}")
print("Digit Frequencies:")
for d in sorted(frequency.keys()):
    print(f" Digit {d}: {frequency[d]} times")
