# Program 22: Custom Multiplier Range Table
# Student: Nitish Kapoor (12625876)

number = 7
start_multiplier = 5
end_multiplier = 15

print(f"Table of {number} from {start_multiplier} to {end_multiplier}:")
for i in range(start_multiplier, end_multiplier + 1):
    print(f"{number} x {i:02d} = {number * i}")
