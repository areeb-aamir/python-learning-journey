# Student Grading System

print("========== STUDENT REPORT SYSTEM ==========\n")

# Student information
name = input("Enter student name: ")
roll_no = input("Enter roll number: ")

print("\nEnter marks out of 100\n")

# Subject marks
math = float(input("Math: "))
english = float(input("English: "))
science = float(input("Science: "))
computer = float(input("Computer: "))
urdu = float(input("Urdu: "))

# Calculations
total = math + english + science + computer + urdu
average = total / 5
percentage = (total / 500) * 100

# Grade system
if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "Fail"

# Final Report
print("\n\n========== FINAL STUDENT REPORT ==========")

print(f"\nName:\t\t{name}")
print(f"Roll No:\t{roll_no}")

print("\n------------- SUBJECT MARKS -------------")

print(f"Math:\t\t{math}")
print(f"English:\t{english}")
print(f"Science:\t{science}")
print(f"Computer:\t{computer}")
print(f"Urdu:\t\t{urdu}")

print("\n-----------------------------------------")

print(f"Total Marks:\t{total} / 500")
print(f"Average:\t{average:.2f}")
print(f"Percentage:\t{percentage:.2f}%")
print(f"Grade:\t\t{grade}")

print("\n=========================================")