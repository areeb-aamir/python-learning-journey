import random
number = random.randint(1, 100)
attempts = 0
while True:
    try:
        guess = int(input("Guess The Number: "))
    except:
        print("Sirf number likho!")
        continue
    if guess == number:
        print("You Won")
        print(f"You Take {attempts + 1} attempts To Win")
        break
    elif guess > number :
        print("It is Big - Try Some Small")
        attempts += 1
    elif guess < number:
        print("It is Small - Try A big One!")
        attempts += 1
