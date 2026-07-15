name = input(f"Enter your name: ")
grade = int(input("Enter your grade (0-100): "))    
print(name.capitalize())
if grade >= 90:
    print("Grade A\nExceptional work; keep pushing boundaries and leading the way.")
elif grade >= 80:
    print("Grade B\nGood job; continue to build on your strengths.")
elif grade >= 70:
    print("Grade C\nSatisfactory performance; there's room for improvement.")
elif grade >= 60:
    print("Grade D\nPassing, but consider seeking additional help.")
else:
    print("Grade F\nFailed. Please consult with your instructor.")
