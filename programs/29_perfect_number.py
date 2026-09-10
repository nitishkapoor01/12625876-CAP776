# Program 29: Perfect Number Check (e.g. 6, 28)
# Student: Nitish Kapoor (12625876)

def is_perfect(n):
    if n <= 1:
        return False
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

print("Check 28 is Perfect:", is_perfect(28))
print("Check 15 is Perfect:", is_perfect(15))

# Perfect numbers under 1000
perfect_under_1000 = [x for x in range(1, 1000) if is_perfect(x)]
print("Perfect numbers < 1000:", perfect_under_1000)
