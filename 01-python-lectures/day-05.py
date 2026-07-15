#Task 10.1


def show_welcome():
    print("Welcome To Student Management System")


show_welcome()    


#task 10.2

database = {}
person = int(input("Number of Peson to add: "))

while True:
    print("Choose Option")
    print("1. Enter Data")
    print("2. Exit")
    option = int(input("Your Option Is: "))
    if option == 1:
        for i in range(person):
            name = input("Enter name: ")
            age = int(input("Enter Age: "))
            city = input("Enter city: ")
            database[i] = {}
            database[i]["Name"] = name
            database[i]["Age"] = age
            database[i]["City"] = city
            break
    elif option == 2:
        break
    else:
        print("Invalid Option!") 
        print("Please Try Again!")  

print("Choose Option")
print("1. Print Dictonary")
print("2. Exit")
dict_print = input("Enter Your Option: ")  
if dict_print == 1:
    print(database)  
else:
    print("GoodBye!")       