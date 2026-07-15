# # Dictnories
# # part 1




# student_dict = {
#     "name" : "Ali",
#     "roll no" : 31,
#     "class" : 10

# }
# print(student_dict["name"])
# print(student_dict["class"])


# # part 2

# stu = {}
# student_dict1 = {
#     "name" : "Ahmed",
#     "roll no" : 14,
#     "class" : 10
# }
# mixed = {
#     "name" : "ALI",
#     "class" : 10,
#     "marks" : [95, 90, 100],
#     "is_active" : True,
#     "score" : 99.5
# }
# print(stu)    
# print(student_dict1)    
# print(mixed)








# # Part 3 


# stu = {
#     "name" : "Ali"
# }
# print(stu.get("name"))
# print(stu.get("city"))
# print(stu.get("city", "not found"))




# # Part 4
# info = {
#     "name" : "Sara",
#     "family_members" : 9,

# }
# print(info)
# info["city"] = "Karachi"
# print(info)
# info["name"] = "soha"
# print(info)
# info.pop("city")
# print(info)
# info.popitem()
# print(info)
# del info["name"]
# print(info)
# info.clear()
# print(info)



# Part 5




# user = {
#     "name" : "Ali",
#     "roll no" : 15,
#     "best teacher" : "deepseek"
# }
# print(user.keys())
# print(user.values())
# print(user.items())
# print(len(user))
# print("name" in user)
# print("Ali" in user)
# print("ss" in user)


# # Part 6


# user = {
#     "name" : "Ali",
#     "roll no" : 15,
#     "best teacher" : "deepseek"
# }
# print(user)
# for keys in user:
#     print(keys)
# for value in user.values():
#     print(value)
# for keys, value in user.items():
#     print(f"{keys} > {value}")




# # Part 7




# info = {
#     "name" : "Ali",
#     "age" : 16,
#     "marks" :{
#         "phy":90,
#         "che" : 90,
#         "bio" : 99
#     },
#     "address" : {
#         "city" : "lahore",
#         "area" : "NEOM"
#     }
# }
# print(info.items())
# print(info["marks"]["bio"])
# print(info["address"]["area"])
# for sub, marks in info["marks"].items():
#     print(f"{sub} > {marks}")




# print("======== Student Database ========")

# students = {}

# for i in range(2):
#     roll = input(f"Enter the roll no of Studnt {i+1}. : ")
#     name = input(f"Enter name of Student({roll}): ")
#     marks = []
#     for j in range(3):
#         mark = int(input(f"Enter Marks obtained in Subject{j+1}: "))
#         marks.append(mark)



#     students[roll] = {
#         "name": name,
#         "marks": marks,
#         "total": sum(marks),
#         "average": sum(marks) / 3
#         }

# print("\n===== All Students =====")
# for roll, data in students.items():
#     print(f"Roll no : {roll}")
#     print(f"  Name: {data['name']}")
#     print(f"  Total: {data['total']}")
#     print(f"  Average: {round(data['average'], 2)}")
#     print("        ---        ")


# # My Task

# students = {}


# for i in range(3):
#     roll = input(f"Enter roll no of Student {i+1}: ")
#     name = input(f"Enter name of student {roll}: ")
#     marks = []
#     for j in range(3):
#         mark = int(input(f"Enter marks of Subject{j+1}: "))
#         marks.append(mark)

#     students[roll] = {"name": name, "marks": marks}


# search_roll = input("Enter roll number to search: ")
# if search_roll in students:
#     print("\n=== Student Found ===")
#     print(f"Name: {students[search_roll]['name']}")
#     print(f"Marks: {students[search_roll]['marks']}")
    
#     # Extra: Har mark alag line mein dikhana (optional)
#     print("Subject Marks:")
#     for i, mark in enumerate(students[search_roll]['marks'], 1):
#         print(f"  Subject {i}: {mark}")
# else:
#     print("Student not found!")