import json

def load_data():
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_data(data):
    with open("students.json", "w") as f:
        json.dump(data, f)


def add_student(student, next_id, name, marks):
    student[next_id] = {"Name" : name, "Marks" : marks}
    save_data(student)
    print("Data Saved!")

def search_student(student, name):
    not_found = False
    for id, info in student.items():
        if name == info["Name"]:
            print(f"Name : {info["Name"]} - Marks : {info["Marks"]}")
            not_found = True
            print("       -----       ")
    if not not_found:
        print("Student Not Found!")
        print("       -----       ")


def delete_data(student, delete):
    for id, info in student.items():
        if delete == info["Name"]:
            del student[id]
            save_data(student)
            print("Student Data Deleted!")
            return
    print(f"{delete}'s Data is Not Exist!")


def show_all(student):
    for id, info in student.items():
        print("===== Students Data ======")
        print(f"ID : {id}")
        print(f"Name : {info["Name"]}")
        print(f"Marks : {info["Marks"]}")
        print("     -----     ")


student = load_data()
while True:
    print("---- Choose Option -----")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Show All")
    print("5. Exit")

    try:
        option = int(input("Your Option: "))
    except ValueError:
        print("Enter Number!")
        print("    ----     ")
        continue
    if option == 1:
        next_id = len(student) + 1
        name = input(f"Enter Name of Student {next_id}: ")
        try:
            marks = int(input(f"Enter Marks of {name}: "))
        except ValueError:
            print("Error! - Enter Only Numbers")
            print("         -------          ")
            continue
        add_student(student, next_id, name, marks)
    elif option == 2:
        search = input("Enter Name To Search: ")
        search_student(student, search)
    elif option == 3:
        delete = input("Enter Name To Delete: ")
        delete_data(student, delete)
    elif option == 4:
        show_all(student)
    elif option == 5:
        print("Thanks For Coming!")
        break
    else:
        print("Invalid Option - Try Again")
