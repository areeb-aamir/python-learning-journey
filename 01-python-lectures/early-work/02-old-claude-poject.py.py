print("======= Welcome to Areeb's Bank =======")

print("              ---------             ")

user_name = "Cloude"
user_password = "112243"
attemt = 0
while attemt < 3:
    name = input("Enter Your Name: ")
    password = input("Enter Your Password: ")
    if name == user_name and password == user_password:
        print("Log In!....")
        break
    else:
        print("Try Again")
        attemt += 1
    if attemt == 3:
        print("Tommorow")
balance = 0
withdraw = 0
deposite = 0
if name == user_name and password == user_password:
    while True:
        print("Choose Any Option")
        
        print("1. Deposite") 
        print("2. Withraw") 
        print("3. Check Balance") 
        print("4. Transaction History")
        print("5. Exit") 
        option = int(input("Enter Your Option: "))                      
        if option == 1:
            deposite = int(input("Enter Deposit amount: ")) 
            balance += deposite
        elif option == 2:
            withdraw = int(input("Entre Ammount to withdraw: "))
            balance -= withdraw 
        elif option == 3:
            print(balance)
        elif option == 4:
            print(f"Your Deposeted Ammount {deposite}")
            print(f"Your Withdraw {withdraw} ")
            print(f"Your Balance is {balance}")
        elif option == 5:
               print("Goodbye!")
               break 
        else:
            print("Invalide Otion")



print("======= Thanks For Comming! =======")

print("              ---------             ")
            