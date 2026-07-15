# # My Task
# database = {}
# students = int(input("Number OF Students You Have : "))

# for i in range(students):
#     name = input("Enter Name: ")
#     marks = int(input(f"Enter Marks of {name}: "))
#     city = input(f"In Which City {name} Lives: ")
#     database[name] = {}
#     database[name]["Marks"] = marks
#     database[name]["City"] = city

# print("======= Student Data =======")



# for name, info in database.items():
#     print(f" Name : {name}")
#     print(f" Marks Obtained : {info['Marks']}")
#     print(f" City : {info['City']}")
#     print("      ------     ")

# all_marks = []
# all_names = []
# for name, info in database.items():
#     all_names.append(name)
#     all_marks.append((info["Marks"]))

# position = all_marks.index(max(all_marks))
# print(f"Topper OF Class Is :{all_names[position]}")




# # lecture 8
# # part 1
# name = "Areeb Aamir"
# print(name)

# # part 2


# name = "Areeb Aamir"



# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())


# # part 3

# name = "Areeb123"
# print(name.isalpha())
# print(name.isnumeric())
# print(name.isalnum())
# print(name.isspace())



# # part 4

# name = " Areeb "
# print(name.strip())
# print(name.lstrip())
# print(name.rstrip())



# # part 5


# sentence = "I love Fareeha and Fareeha is Great"
# print(sentence.find("Fareeha"))
# print(sentence.count("Fareeha"))
# print(sentence.replace("Fareeha", "anya"))
# print(sentence.replace("Fareeha", "anya", 1))




# # part 6 
# sentence = "Areeb,Ali,Taha,Hassan"
# print(sentence.split(","))
# print(sentence.split(",", 2))
# sentence_2 = "Areeb Is Good Boy"
# print(sentence_2.split())
# print(sentence_2.split(" ", 2))


# #

# names = ["Areeb", "Ali", "Taha"]
# result = " , ".join(names)
# print(result)
# result = " - ".join(names)
# print(result)

# # part 7


# email = "areeb1122@gmail.com"
# print(email.startswith("areeb"))
# print(email.endswith(".com"))
# print(email.endswith("pk"))




# # part 8
# name = "Areeb Aamir"
# print(len(name))
# print("Areeb" in name)
# print("areeb" in name)





# # My Task


# print("====== Email Checker =======")
# email = input("Enter Your Gmail: ").strip().lower()
# check = "@" in email
# check_2 = email.endswith("@gmail.com")


# if check and check_2:
#     print("Your Email is Correct")
# else:
#     print("Wrong Gmail!")    




# Leture 9

try:
    age = int(input("Enter age: "))
    print(f"Tumhari umar: {age}")
except:
    print("Sirf number type karo!")























