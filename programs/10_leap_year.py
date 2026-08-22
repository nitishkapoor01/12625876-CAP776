# Program 10: Check Leap Year
# Student: Nitish Kapoor (12625876)

year = 2024

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(f"Year {year} is a Leap Year.")
else:
    print(f"Year {year} is NOT a Leap Year.")
