# Program 06: Calculate Simple Interest
# Student: Nitish Kapoor (12625876)

principal = 15000.0  # Amount in Rupees
rate = 6.5           # Annual interest rate %
time = 3             # Time in years

si = (principal * rate * time) / 100
total_amount = principal + si

print(f"Principal Amount : Rs. {principal:.2f}")
print(f"Simple Interest  : Rs. {si:.2f}")
print(f"Total Maturity   : Rs. {total_amount:.2f}")
