#making an expense tracker app
breakfast = int(input("Enter the amount spent on breakfast: "))
lunch_cost= int(input("Enter the amount spent on lunch: "))
dinner_cost = int(input("Enter the amount spent on dinner: "))
total_spent = breakfast + lunch_cost + dinner_cost
print("Total amount spent on food: ", total_spent)
print("Breakfast cost: ", breakfast)
print("Lunch cost: ", lunch_cost)
print("Dinner cost: ", dinner_cost)
if breakfast > lunch_cost and breakfast > dinner_cost:
    print("You spent a lot on breakfast!")
elif lunch_cost > breakfast and lunch_cost > dinner_cost:
    print("You spent a lot on lunch!")
elif dinner_cost > breakfast and dinner_cost > lunch_cost:
    print("You spent a lot on dinner!")
else:    
    print("Your expenses are balanced across meals.")