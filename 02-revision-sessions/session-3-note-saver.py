text = input("Enter Text To Save In File: ")

with open("notes.txt", "a") as f:
    f.write(f"{text}\n")


try:
    with open("notes.txt", "r") as f:
        content = f.read()
        print(" === File Content === ")
        print(content)
except FileNotFoundError:
    print("File Not Found!")
