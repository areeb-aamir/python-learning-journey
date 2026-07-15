# class student:
#     pass
# areeb = student()
# ali = student()
# print(student)

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks


# areeb = student("Areeb", 80)
# ali = student("Ali", 90)
# print(areeb.name)
# print(ali.marks)
# print(areeb.marks)






# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def show_info(self):          # self yahan bhi chahiye
#         print(f"Name: {self.name}, Marks: {self.marks}")

# areeb = Student("Areeb", 95)
# areeb.show_info()   # Name: Areeb, Marks: 95




# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def get_grade(self):
#         if self.marks >= 90:
#             return "A"
#         elif self.marks >= 80:
#             return "B"
#         elif self.marks >= 70:
#             return "C"
#         else:
#             return "F"
    
#     def show_info(self):
#         grade = self.get_grade()   # ek method dusre method ko call kar sakta hai
#         print(f"Name: {self.name} — Marks: {self.marks} — Grade: {grade}")
#         print("       -----       ")

  
# students = [
#     Student("Areeb", 95),
#     Student("Ali", 65),
#     Student("Hassan", 45)
# ]

# for s in students:
#     s.show_info()




# class Car:
#     def __init__(self, brand, model, price):
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def show_details(self):
#         print(f"Brand : {self.brand} - Model : {self.model} - Price : {self.price}")

#     def apply_discount(self, percent):
#         self.price = (self.price*(100-percent)/100)


# car1 = Car("Tesla", "A4", 45000)
# car1.show_details()
# car2 = Car("BMW", "M5", 145000)
# car2.show_details()
# car3 = Car("Buggati", "Chirone", 545000)
# car3.show_details()
# car3.apply_discount(50)
# car3.show_details()






# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     def show_details(self):
#         print(f"Name : {self.name}, Salary : {self.salary}")

# class Manager(Employee):
#     def __init__(self, name, salary, team_size):
#         super().__init__(name, salary)
#         self.team_size = team_size
#     def show_details(self):
#         print(f"Name : {self.name}, Salary : {self.salary}, Team Size : {self.team_size}")



# employee = Employee("Ali", 60000)
# employee.show_details()
# manager = Manager("Ahmed", 90000, 5)
# manager.show_details()



# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance   # private — do underscore
    
#     def show_balance(self):
#         print(f"Balance: {self.__balance}")

# account = BankAccount(1000)
# # print(account.__balance)   
# account.show_balance()     



# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance
    
#     def get_balance(self):              # Getter — value nikalne ke liye
#         return self.__balance
    
#     def deposit(self, amount):          # Setter jaisa — safely add karne ke liye
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Galat amount!")
    
#     def withdraw(self, amount):
#         if amount > self.__balance:
#             print("Itna balance nahi hai!")
#         else:
#             self.__balance -= amount

# account = BankAccount(1000)
# account.deposit(500)
# print(account.get_balance())   # 1500

# account.withdraw(300)         # Itna balance nahi hai!
# print(account.get_balance())






# class Wallet:
#     def __init__(self, balance):
#         self.__balance = balance

#     def add_amount(self, balance):
#         if balance < 0:
#             print("Wrong Amount!")
#         else:
#             self.__balance += balance
    
#     def spend_amount(self, balance):
#         if balance > self.__balance:
#             print("Insufficient balance!")
#         else:
#             self.__balance -= balance

#     def show_amount(self):
#         print(f"Your Balance Is : {self.__balance}")

# account = Wallet(1000)
# account.show_amount()
# account.add_amount(-1000)
# account.show_amount()
# account.add_amount(1000)
# account.show_amount()
# account.spend_amount(3000)
# account.show_amount()
# account.spend_amount(1000)
# account.show_amount()





# class Shape:
#     def area(self):
#         print("Area calculate nahi ho sakta — shape define nahi")

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def area(self):
#         print(f"Circle Area: {3.14 * self.radius ** 2}")

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         print(f"Rectangle Area: {self.length * self.width}")

# shapes = [Circle(5), Rectangle(4, 6)]

# for shape in shapes:
#     shape.area()    # har shape apna area calculate karega




# class CreditCard:
#     def __init__(self):
#         pass
#     def process_payment(self, amount):
#         print(f"Rs. {amount} credit card se pay ho gaya")
# class PayPal:
#     def __init__(self):
#         pass
#     def process_payment(self, amount):
#         print(f"Rs. {amount} PayPal se pay ho gaya")
# class BankTransfer:
#     def __init__(self):
#         pass
#     def process_payment(self, amount):
#         print(f"Rs. {amount} bank transfer se pay ho gaya")


# payment = [CreditCard(), PayPal(), BankTransfer()]
# for p in payment:
#     p.process_payment(5000)
    





# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     def __str__(self):
#         return f"Name : {self.name} , Marks : {self.marks}"

# areeb = Student("Areeb", 95)
# print(areeb)
# # <__main__.Student object at 0x7f8b2c0a1d90>   ← bekaar output

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def __eq__(self, other):
#         return self.marks == other.marks

# s1 = Student("Areeb", 95)
# s2 = Student("Ali", 95)

# print(s1 == s2)   # True — kyunke marks barabar hain




# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages
    

#     def __str__(self):
#         return f"{self.title} BY {self.author} Having {self.pages} Pages"

#     def __len__(self):
#         return self.pages
    
#     def __eq__(self, other):
#         return self.title == other.title



# book = Book("Sucess", "Elon Musk", 100)
# bood = Book("Love", "MJ", 150)
# print(book)
# print(len(book))
# print(book == bood)




# class MathHelper:
#     @staticmethod
#     def add(a, b):
#         return a + b

# result = MathHelper.add(5, 3)   # object banaye bina call ho gaya!
# print(result)   # 8





class Product:
    total_products = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.total_products += 1

    @classmethod
    def get_total_product(cls):
        return f"Total Product Are : {Product.total_products}"

    @staticmethod
    def is_price_valid(price):
        return price > 0

p1 = Product("Laptop", 50000)
p2 = Product("Mouse", 1000)
p3 = Product("Keyboard", 2000)

print(Product.get_total_product())     
print(Product.is_price_valid(-100))      































































































































































