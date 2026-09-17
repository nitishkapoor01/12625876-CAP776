# Program 36: ATM Menu-Driven Simulation
# Student: Nitish Kapoor (12625876)

balance = 10000.0

def deposit(amount):
    global balance
    if amount > 0:
        balance += amount
        print(f"Deposited Rs. {amount:.2f}. New Balance: Rs. {balance:.2f}")

def withdraw(amount):
    global balance
    if 0 < amount <= balance:
        balance -= amount
        print(f"Withdrawn Rs. {amount:.2f}. Remaining Balance: Rs. {balance:.2f}")
    else:
        print("Invalid amount or Insufficient Balance!")

print("Initial Balance: Rs. ", balance)
deposit(2500)
withdraw(4000)
withdraw(15000)  # Overdraw test
