

# print("===== Classic Login System =====")

# def cal_sum(num1, num2, opretion = "add"):
#     if opretion == "add":
#         return num1 + num2
#     elif opretion == "subtract" or opretion == "sub":
#         return num1 - num2
#     elif opretion == "multiply" or opretion == "mul":
#         return num1 * num2
#     elif opretion == "divide" or opretion == "div":
#         return num1 / num2
#     else:
#         return "Invalid operation"


# your_operation = cal_sum(int(input("First number: ")), int(input("Second number: ")), input("Operation (add/subtract/multiply/divide): "))
# print(your_operation)




# # task 5

# print("=====Prime Number Checker=====")
# def num(num):
#     if num == 0:
#         return "Not a prime number"
#     elif num == 1:
#         return "Not a prime number"
#     elif num == 2:
#         return "Prime number"
#     elif num > 2:
#         for i in range(2, num):
#             if num % i == 0:
#                 return "Not a prime number"
#         return "Prime number" 
#     else:
#         return "Invalid input"
# check_num = int(input("Enter a number to check if it's prime or not: "))
# print(num(check_num))           
    







#  #********lists******


#  # part 1
# fruits = ["mango", "apple", "banana"]
# print(fruits[1])



# # part 2



# fruits = ["apple", "banana", "mango", "orange"]
# #indexes:     0         1         2        3

# print(fruits[0])    # apple
# print(fruits[1])    # banana
# print(fruits[3])    # orange
# print(fruits[-1])   # orange — ulti side se pehla
# print(fruits[-2])   # mango — ulti side se doosra





# # part 3

# fruits = ["mango", "apple", "banana", "orange"]
# print(fruits)

# fruits.append("melon")
# print(fruits)

# fruits.insert(1, "grapes")
# print(fruits)

# fruits.remove("banana")
# print(fruits)



# fruits.pop()
# print(fruits)
# fruits.pop(2)
# print(fruits)

# print(len(fruits))
# fruits.sort()
# print(fruits)

# fruits.sort(reverse = True)
# print(fruits)


# print("apples" in fruits)
# print("grapes"in fruits)



# # part 4




# fruits = ["apple", "banana", "orange"]
# for i in fruits:
#     print(f"fruits hai :{i}")


# for i in range(len(fruits)):
#     print(f"{i}.{fruits[i]}")


# # part 5
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(num[0:5])
# print(num[4:9])
# print(num[:6])
# print(num[6:])
# print(num[::3])
# print(num[::-1])
# print(num[2:10:3])
# print(num[10:0:-2])





# part 6

print("=====Students Marks System=====")
students = []
marks = []


for i in range(3): 
    name = input(f"Name of Student {i+1} is: ")
    mark = int(input(f"{name} has Marks:"))
    students.append(name)
    marks.append(mark)   
print("\n==== Results ====")
for i in range(len(students)):
    print(f"{students[i]} : {marks[i]}")


print(f"\n Higgest Marks : {max(marks)}")
print(f"Lowest Marks : {min(marks)}")
print(f"Average : {sum(marks)/len(marks)}")




# # My Project


# print("======= Your Data =======")
# numbers = []
      
# for i in range(5):
#     num = int(input("Enter Number : "))
#     numbers.append(num)


# print("======= Simple Statistics =======")
# print(f"The sum is : {sum(numbers)}")
# print(f"The Higgest Number is : {max(numbers)}")
# print(f"The Lowest Number is : {min(numbers)}")
# print(f"The Average is : {sum(numbers)/len(numbers)}")
