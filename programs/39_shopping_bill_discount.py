# Program 39: Shopping Bill with Tiered Discounts
# Student: Nitish Kapoor (12625876)

def calculate_final_bill(total_amount):
    if total_amount >= 10000:
        discount = 0.20
    elif total_amount >= 5000:
        discount = 0.10
    elif total_amount >= 2000:
        discount = 0.05
    else:
        discount = 0.0

    discount_amount = total_amount * discount
    final_payable = total_amount - discount_amount
    return discount_amount, final_payable

bills = [12000, 7500, 3000, 1500]
for b in bills:
    disc, payable = calculate_final_bill(b)
    print(f"Bill: Rs. {b} | Discount: Rs. {disc:.2f} | Final: Rs. {payable:.2f}")
