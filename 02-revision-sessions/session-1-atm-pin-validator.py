pass_code = 1234
attemts = 0
print("--------- Login System -------")
print("          ------------      ")
while attemts <= 3:
    password = int(input("Enter Password of 4 Numbers: ").strip())
    if len(str(password)) == 4 :
        if password == pass_code :
            print("Welcome!")
            break
        else:
            print("Invalid Password - Try Again!")
            attemts += 1
    else:
        print("Try Again - Only 4 Numbers Allowed")

if attemts == 4:
    print("Account Blocked!")
