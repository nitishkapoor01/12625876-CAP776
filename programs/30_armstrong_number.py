# Program 30: Armstrong Number Check and Range Search
# Student: Nitish Kapoor (12625876)

def is_armstrong(num):
    s = str(num)
    p = len(s)
    return sum(int(c)**p for c in s) == num

print("Is 153 Armstrong? ->", is_armstrong(153))
print("Is 370 Armstrong? ->", is_armstrong(370))

armstrong_under_1000 = [x for x in range(1, 1000) if is_armstrong(x)]
print("Armstrong numbers < 1000:", armstrong_under_1000)
