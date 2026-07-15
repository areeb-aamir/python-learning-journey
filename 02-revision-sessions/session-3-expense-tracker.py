total = 0
while True:
    print("---- Choose Option -----")
    print("1. Add Expences In Database")
    print("2. Exit")
    try:
        option = int(input("Enter Your Option: "))
    except ValueError:
        print("Error! - Enter Number")
        print("      -----      ")
        continue
    if option == 1:
        expence = input("Entre Name of Expence:")
        try:
            cost = int(input(f"Enter Cost You Spend On {expence}: "))
            total += cost
            with open ("expence.txt", "a") as f:
                f.write(f"{expence} : ${cost}\n")
                print("Data Saved")
        except ValueError:
            print("Error! - Enter Number Next Time")
            print("         -------        ")
            continue

    elif option == 2:
        print(f"Your Total Ammount Spend Is ${total}.")
        break
    else:
        print("Invalid Input")
