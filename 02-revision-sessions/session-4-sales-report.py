sales = [
    {"buyer": "Areeb", "product": "Laptop", "amount": 150000, "category": "Electronics"},
    {"buyer": "Ali", "product": "Shirt", "amount": 2500, "category": "Clothing"},
    {"buyer": "Areeb", "product": "Mouse", "amount": 2500, "category": "Electronics"},
    {"buyer": "Hassan", "product": "Jeans", "amount": 4500, "category": "Clothing"},
    {"buyer": "Ali", "product": "Headphones", "amount": 12000, "category": "Electronics"},
    {"buyer": "Zara", "product": "Laptop", "amount": 150000, "category": "Electronics"},
]

unique = {s["buyer"] for s in sales }
print(unique)
expencive = [s["product"] for s in sales if s["amount"] > 10000]
print(expencive)
totals = {buyer: sum(s["amount"] for s in sales if s["buyer"] == buyer)
          for buyer in {s["buyer"] for s in sales}}
print(totals)
category = {s["category"] for s in sales}
print(category)
