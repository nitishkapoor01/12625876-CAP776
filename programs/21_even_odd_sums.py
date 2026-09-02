# Program 21: Sum of Even and Odd Numbers from 1 to N
# Student: Nitish Kapoor (12625876)

n = 20
even_sum = 0
odd_sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print(f"1 to {n} -> Sum of Even Numbers: {even_sum}")
print(f"1 to {n} -> Sum of Odd Numbers : {odd_sum}")
