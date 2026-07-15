# # Sets
# # part 1 - Set


# visitor_set = {"Areeb", "Ali", "Hassan", "Areeb"}
# print(visitor_set)


# # part 2 - Set Making


# # 1. curley Braces
# languages = {"Python", "C++", "Java", "MongoDB"}
# print(languages)

# # 2. sets-list

# languages = set(["Python", "C++", "Java", "MongoDB"])
# print(languages)


# # 3. remove duplicate from lists

# names = ["Areeb", "Ali", "Hassan", "Ali"]
# print(set(list)) 


# # 4. Empty set

# empty_set = set()


# # part 3 - Set methods


# languages = {"Python", "C++", "Java", "MongoDB"}
# languages.add("Doctor")
# print(languages)
# languages.remove("C++")
# print(languages)
# languages.discard("JS")
# print(languages)
# print("Python" in languages)
# print("JS" in languages)

# print(len(languages))
# languages.clear()
# print(languages)



# # part 4 - set Operations


# group_A = {"Ali", "Areeb", "Hashir", "Hassan" } 
# group_B = {"Fareeha", "Areeb", "Anya", "Zoya" } 
# common = group_A & group_B
# print(common)
# common_2 = group_A | group_B
# print(common_2)
# only_group_A = group_A - group_B
# print(only_group_A)
# only_group_B = group_B - group_A
# print(only_group_B)
# not_common = group_A ^ group_B
# print(not_common)






# # part 5 - All


# def clean_emails_list(emails):
#     total = len(emails)
#     unique = set(emails)
#     duplicate_found = total - len(unique)
    
#     print(f"Total Emails : {total}")
#     print(f"Duplicate : {duplicate_found}")
#     print(f"Clean Emails : {len(unique)}")
#     return sorted(list(unique))

# emails = [
#     "areeb@gmail.com",
#     "ali@gmail.com",
#     "areeb@gmail.com",
#     "hassan@gmail.com",
#     "ali@gmail.com"
# ]

# clean = clean_emails_list(emails)
# print(clean)

# # MY Task

# week1_buyers = ["Areeb", "Ali", "Hassan", "Zara", "Areeb", "Ali"]
# week2_buyers = ["Hassan", "Bilal", "Zara", "Usman", "Areeb"]



# week1_buyers_set = set(week1_buyers)
# week2_buyers_set = set(week2_buyers)
# print(week1_buyers_set)
# common = week1_buyers_set & week2_buyers_set
# print(common)
# new_buyers = week2_buyers_set - week1_buyers_set
# print(new_buyers)
# unique = week1_buyers_set | week2_buyers_set
# print(unique)



# # 11.3


# # tuple formation


# name = ("Areeb", "Aamir", "Ali")
# print(name)
# name = "Areeb", "Aamir", "Ali"
# print(name)
# name = ["Areeb", "Aamir", "Ali"]
# print(tuple(name))
# name = ("Areeb",)
# print(name)
# name = ()



# # indz and slicing


# name = ("Areeb", "Aamir", 23, "Ali")

# print(name[-1])
# print(name[1:3])
# print(name[:3])
# print(name[1:])

# print(name[:3])
# print(len(name))
# print("Areeb" in name)
# print("24" in name)



# # best funtion

# person = ("Areeb", 23, "Los Angeles")
# name, age, city, = person


# print(name)
# print(age)
# print(city)



# def get_coordinates():
#     return (31.5497, 74.3436)

# lat, lng = get_coordinates()
# print(f"Latitude: {lat}")
# print(f"Longitude: {lng}")

# num = (1, 2, 3, 4, 5, 6, 7, 8, 9,)
# first, *rest, any, ani, ahu = num
# print(first)
# print(rest)




# def get_student(name, marks, grade):
#     return (name, marks, grade)   # tuple return kar raha hai

# def print_student(record):
#     name, marks, grade = record   # unpack kiya
#     print(f"Naam    : {name}")
#     print(f"Marks   : {marks}")
#     print(f"Grade   : {grade}")
#     print("-" * 25)

# # Records banao
# students = [
#     get_student("Areeb", 95, "A+"),
#     get_student("Ali", 78, "B"),
#     get_student("Hassan", 60, "C"),
# ]

# # Sab print karo
# for student in students:
#     print_student(student)

# # Top student nikalo
# top = max(students, key=lambda s: s[1])
# print(f"Top Student: {top[0]} — {top[1]} marks")





students = [
    {"name": "Areeb", "marks": 95},
    {"name": "Ali", "marks": 42},
    {"name": "Hassan", "marks": 78},
    {"name": "Zara", "marks": 55},
    {"name": "Bilal", "marks": 30},
]

passed = [name for name, marks in students if marks >= 90]
print(f"Pass students: {passed}")











