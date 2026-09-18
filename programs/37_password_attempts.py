# Program 37: Password Lockout Simulation (3 Attempts)
# Student: Nitish Kapoor (12625876)

CORRECT_PASS = "admin123"
attempts_log = ["wrong1", "wrong2", "admin123"]
max_attempts = 3

for attempt, entry in enumerate(attempts_log, start=1):
    if entry == CORRECT_PASS:
        print(f"Attempt {attempt}: Access Granted!")
        break
    else:
        remaining = max_attempts - attempt
        print(f"Attempt {attempt}: Incorrect Password! ({remaining} attempts left)")
        if remaining == 0:
            print("Account Locked! Please try again later.")
