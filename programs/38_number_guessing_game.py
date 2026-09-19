# Program 38: Number Guessing Logic
# Student: Nitish Kapoor (12625876)

SECRET = 42
guesses = [20, 60, 35, 45, 42]

for idx, g in enumerate(guesses, start=1):
    if g < SECRET:
        print(f"Guess {idx} ({g}): Too Low!")
    elif g > SECRET:
        print(f"Guess {idx} ({g}): Too High!")
    else:
        print(f"Guess {idx} ({g}): Correct! Found secret number in {idx} tries.")
        break
