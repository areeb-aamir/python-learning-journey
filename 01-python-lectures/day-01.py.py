print("Hello, World!")
print("Welcome to Python programming.")
print("This is the first lecture.")


naam = "Taha"
umar = 21
city = "Lahore"

print(naam)
print(umar)
print(city)
print("Mera naam hai:", naam)
print("Meri umar hai:", umar)
print("Main rehta hun:", city)
naam = "Taha"          # ye str hai
umar = 21             # ye int hai
height = 5.8           # ye float hai

print(type(naam))      # <class 'str'>
print(type(umar))      # <class 'int'>
print(type(height))    # <class 'float'>
naam = input("Apna naam batao: ")
print("Wa alaikum assalam,", naam)


name = input("Apna naam batao: ")
age = input("Apni umar batao: ")
favourite_Game = input("Apna favourite game batao: ")
print("=== Your Information ===")
print("name :", name)
print("age :", age)
print("favourite_Game :", favourite_Game)




num1 = int(input("Pehla number: "))
num2 = int(input("Doosra number: "))
print(num1 + num2)


name = str(input("Apna naam batao: "))
age = int(input("Apni umar batao: "))   
print(f"your name is {name} and age is {age}")




num1 = float(input("First_number: "))
num2 = float(input("Second_number: "))
print("=============Basic Arthematic Operations=============")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")
print(f"{num1} / {num2} = {num1 / num2}")



height = float(input("enter your height in feets: "))
height_in_cm = height * 30.48
print("======Height Converter======")
print (f"your height in cm is: {round(height_in_cm, 2)} cm")





umar = int(input("enter your age: "))
id_card = bool(input("do you have an id card? (True/False): "))

if umar >= 18 and id_card:
    print("You can Entre!")
else:
    print("No Entry!")




print("======Sign Check=====")
num = int(input("Enter a number: "))
if num > 0 :
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



print("=== Login System ===")

username = str(input("Username daalo: "))
password = int(input("Password daalo: "))

if username == "admin" and password == 1234:
    print("Login successful! Welcome!")
else:
    print("Wrong username or password!")                                  






# loop Practice


# part 1


count = 1
while count <= 5 :
    print (f"count is : {count}")
    count += 1


# Part2


for i in range(5):
    print(f"number is : {i}")


# part 3


number = int(input("Enter a number to print its multiplication table: "))
for i in range(1,6):
    print(f" {number} * {i} = {number*i}")  



# part 4


for i in range (1, 11):
    if i == 5:
        break
    print(f"number is : {i}")


# part 5



for i in range (1, 11):
    if i == 3:
        continue
    print(f"number is : {i}")



# part 6

print("=== Guess the Number ===")

secret = 7
attemts = 0


while True:
    guess = int(input("Guess the number between 1 and 10: "))
    attemts += 1
    if guess == secret:
        print(f"Congratulations! You guessed the number in {attemts} attempts.")
        break
    elif guess < secret:
        print("num is too low. Try again.")
    else:
        print("num is too high. Try again.")    

# my Practice

for i in range (1, 101):
    if i % 7 == 0:
        print(f"{i}")
   