# Program 44: Mini Student Marks Analyzer System
# Student: Nitish Kapoor (12625876)

students = [
    {"roll": 101, "name": "Nitish Kapoor", "marks": [92, 88, 85, 90, 95]},
    {"roll": 102, "name": "Aman Sharma", "marks": [78, 82, 80, 75, 84]},
    {"roll": 103, "name": "Rohan Verma", "marks": [45, 52, 48, 50, 55]}
]

print("--- STUDENT MARKS ANALYZER ---")
percentages = []

for s in students:
    total = sum(s["marks"])
    pct = total / 5.0
    percentages.append(pct)
    grade = "A+" if pct >= 85 else ("A" if pct >= 75 else "Pass")
    print(f"Roll {s['roll']} | {s['name']} -> Total: {total}/500, Pct: {pct:.1f}%, Grade: {grade}")

print(f"\nClass Average : {sum(percentages)/len(percentages):.2f}%")
print(f"Highest Scorer: {max(percentages):.2f}%")
print(f"Lowest Scorer : {min(percentages):.2f}%")
