# Program 20: Positive, Negative, or Zero Counter
# Student: Nitish Kapoor (12625876)

numbers = [12, -5, 0, 45, -23, 0, 89, -1, 0, 34]
pos_count, neg_count, zero_count = 0, 0, 0

for num in numbers:
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1
    else:
        zero_count += 1

print("Numbers List :", numbers)
print("Positive Count:", pos_count)
print("Negative Count:", neg_count)
print("Zero Count    :", zero_count)
