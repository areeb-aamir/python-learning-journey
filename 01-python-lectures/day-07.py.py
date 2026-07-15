# # Part 1 — try / except



# try:
#     age = int(input("Enter Your Age: "))
# except:
#     print("Enter  Number!")




# # part 2


# try:
#     num = int(input("Enter NUmber:"))
#     print(100/num)
# except ValueError:
#     print("Type a Number")
# except ZeroDivisionError:
#     print("Cantt Divide By Zero")    




# # part 3


# try:
#     num = int(input("Enter A Number: "))
#     result = 100/num
# except ValueError:
#     print("Type A Number")
# except ZeroDivisionError:
#     print("Cantt Divide by zero")
# else:
#     print(f"result is : {result}")
# finally:
#     print("Programme Finish")   



# # part 4


# while True:
#     try:
#         age = int(input("Enter Yor Age: "))
#         break
#     except ValueError:
#         print("It is not a Number - Try Again!")
# print(f"Your Age is : {age}")




# # part 5
# students = {
#     "Areeb" : 75,
#     "Ali" : 44
# }


# while True:
#     try:
#         name = input("Enter Name Of Student: ").capitalize()
#         print(students[name])
#         break
#     except KeyError:
#         print("This Student Is Not In Your Database - Try Again!")
#     finally:
#         print("Thanks!")



# # My Task


# print("===== Classic Login System =====")

# def cal_sum(num1, num2, opretion = "add"):
#     if opretion == "add":
#         return num1 + num2
#     elif opretion == "subtract" or opretion == "sub":
#         return num1 - num2
#     elif opretion == "multiply" or opretion == "mul":
#         return num1 * num2
#     elif opretion == "divide" or opretion == "div":
#         if num2 == 0:
#             return("We Cantt Divide By Zero")
#         return num1 / num2
#     else:
#         return "Invalid operation"


# while True:
#     try:    
#         num_1 = int(input("Enter First Number: "))
#         break
#     except ValueError:
#         print("Try Again With a Number!")

# while True:
#     try:    
#         num_2 = int(input("Enter Second Number: "))
#         break
#     except ValueError:
#         print("Try Again With a Number!")


# while True:
#     operation = input("Operation (add/sub/mul/div): ")
#     result = cal_sum(num_1, num_2, operation)
#     if result == "Invalid operation":
#         print("Your Operation IS Wrong - Try Again")
#     else:
#         print(f" result is : {result}") 
#         break   




# # lecture 10

# #بِسْمِ ٱللّٰهِ ٱلرَّحْمٰنِ ٱلرَّحِيمِ


# # part 1 


# file = open("data.txt", "w")
# file.write("Areeb Aamir\n")
# file.write("Lahore\n")
# file.close


# # part 2

# with open("data.txt", "a") as file:
#     file.write("Areeb Aamir\n")
#     file.write("Lahore\n")


# # part 3


# with open("data.txt", "r") as file:
#     content = file.read()
#     print(content)
# with open("data.txt", "r") as file:
#     line = file.readline()
#     print(line)
# with open("data.txt", "r") as file:    
#     lines = file.readlines()
#     print(lines)


# # part 4



# with open("data.txt", "a") as file:
#     file.write("Python Developer\n")










# # part 5
# with open ("data.txt", "r") as file:
#     for line in file:
#         print(line.strip())




















# # part 6

# try:
#     with open ("data.txt", "r") as file:
#         content = file.read()
#         print(content)
        
# except FileNotFoundError:
#     print("file not found")        







# # part 7


# def save_note(note):
#     with open ("note.txt", "w") as file:
#         file.write(note + "\n")
    

# def show_note():
#     try:
#         with open("note.txt", "r") as file:
#             content = file.read()
#             print(content)
#     except FileNotFoundError:
#         print("file not found")


# while True:
#     choice = input("1-Add Note  2-Show Notes  3-Exit: ")
#     if choice == "1":
#         note = input("Enter Note To Add: ")
#         save_note(note)
#     elif choice == "2":
#         show_note()
#     elif choice == 3:
#         break
#     else:
#         print("Invalid Option - Try Again!")








# My Task


def save_note(key, value):
    with open ("contactbook.txt", "a") as file:
        file.write(f"{key} : {value}\n")
    

def show_note():
    try:
        with open("contactbook.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("file not found")



def search_contact(name):
    with open("contactbook.txt", "r") as file:
        for line in file:
            if name in line:
                print(line.strip())






while True:
    choice = input("1-Add Note  2-Show Notes  3-Search Contract 4- Exit: ")
    if choice == "1":
        key = input("Enter Name: ")
        value = input("Enter Contract Number: ")
        save_note(key, value)
    elif choice == "2":
        show_note()
    elif choice == "3":
        name = input("Enter Name: ")
        search_contact(name)
    elif choice == "4":
        break
    else:
        print("Invalid Option - Try Again!")











