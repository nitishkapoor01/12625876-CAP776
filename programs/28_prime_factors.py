# Program 28: Prime Factors of a Number (Including Repeated)
# Student: Nitish Kapoor (12625876)

num = 84
temp = num
factors = []

d = 2
while d * d <= temp:
    while temp % d == 0:
        factors.append(d)
        temp //= d
    d += 1
if temp > 1:
    factors.append(temp)

print(f"Prime factors of {num} are: {factors}")
