# Program 11: Display Grades using If-Elif-Else
# Student: Nitish Kapoor (12625876)

marks = 84.5

if marks >= 90:
    grade = "A+ (Outstanding)"
elif marks >= 80:
    grade = "A (Excellent)"
elif marks >= 70:
    grade = "B (Very Good)"
elif marks >= 60:
    grade = "C (Good)"
elif marks >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

print(f"Marks: {marks} -> Assigned Grade: {grade}")
