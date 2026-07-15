expenses = {
    "Food": [],
    "Transport": [],
    "Shopping": [],
}

budgets = {
    "Food": 5000,
    "Transport": 2000,
    "Shopping": 3000
}


    print("\n===== Personal Finance Dashboard =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Summary")
    print("4. Budget Status")
    print("5. Exit")

    choice = input("\nChoose option: ")

    if choice == "1":
        print("\n--- Adding Expense ---")
        amount = int(input("Enter amount: "))
        category = input("Enter category (Food/Transport/Shopping): ")

        expenses[category].append(amount)

        print(f"✓ Added {amount} to {category}")
        print(f"Current {category} expenses: {expenses[category]}")

    elif choice == "2":
        print("\n--- All Expenses ---")

        for category in expenses:
            print(f"\n{category}:")
            if len(expenses[category]) == 0:
                print("  No expenses yet")
            else:
                for amount in expenses[category]:
                    print(f"  - {amount} PKR")

    elif choice == "3":
        print("\n--- Category Summary ---")

        total_spending = 0

        for category in expenses:
            category_total = sum(expenses[category])
            num_transactions = len(expenses[category])

            print(f"{category}: {category_total} PKR ({num_transactions} transactions)")

            total_spending = total_spending + category_total

        print(f"\nTotal Spending: {total_spending} PKR")

    elif choice == "4":
        print("\n--- Budget Status ---")

        for category in expenses:
            spent = sum(expenses[category])
            budget = budgets[category]
            percentage = (spent / budget) * 100

            print(f"{category}: {spent} / {budget} PKR ({percentage:.1f}% used)")

            if spent > budget:
                print(f"  ⚠️ OVER BUDGET by {spent - budget} PKR!")
            elif percentage >= 80:
                print(f"  ⚠️ Warning: Approaching limit!")
            else:
                print(f"  ✓ Within budget")

    elif choice == "5":
        print("\nGoodbye!")

    else:
        print("\n Invalid option. Please choose 1-5.")
