# its my First project and may it will be good 



print("========= Class result Maker ==========")



students = []
marks = []
for i in range(3):
    name = input(f"Enter the Name of {i+1}. Student: ")
    students.append(name)
    student_marks = []
    for j in range(3):
        mark = int(input(f"Enter Marks of Subject {i+1} of Student {name} out of 100: "))
        student_marks.append(mark)
    marks.append(student_marks)

    
       
def result(mark1 ,mark2 ,mark3):
    total = (mark1 + mark2 + mark3)
    average = (total/3)
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
    return total, average, grade 


for i in range(3):
    total, average, grade = result(marks[i][0], marks[i][1], marks[i][2])
    print(f"{students[i]} ka total: {total}")
    print(f"{students[i]} ka average: {round(average, 2)}")
    print(f"{students[i]} ka grade: {grade}")
    print("---")

topper = students[marks.index(max(marks))]

print(f"The Class Topper is {topper}")