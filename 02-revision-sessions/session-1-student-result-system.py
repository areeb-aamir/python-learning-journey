for i in range(3):
    name = input(f"Enter Name of Student {i+1}: ")
    total = 0
    for j in range(3):
        marks = int(input(f"Enter Marks Of {name} of Subject {j+1}: "))
        total = total + marks
    average = total/3
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    print("-" * 30)
    print(f"Student  : {name}")
    print(f"Average  : {average:.1f}")  # 80.0 ki jagah 80.3 style
    print(f"Grade    : {grade}")
    print("-" * 30)



