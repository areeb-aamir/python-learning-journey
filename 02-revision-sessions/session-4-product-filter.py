products = [
    {"name": "Laptop", "price": 150000, "category": "Electronics", "stock": 5},
    {"name": "Phone", "price": 80000, "category": "Electronics", "stock": 0},
    {"name": "Shirt", "price": 2500, "category": "Clothing", "stock": 15},
    {"name": "Headphones", "price": 12000, "category": "Electronics", "stock": 3},
    {"name": "Jeans", "price": 4500, "category": "Clothing", "stock": 8},
]



in_stock = [p["name"] for p in products if p["stock"] > 0]
print(in_stock)
e_catogary = [p["name"] for p in products if p["category"] == "Electronics" ]
print(e_catogary)
expencive = {p["name"]: p["price"] for p in products if p["price"] > 10000}
print(expencive)
categories = {p["category"] for p in products}
print(categories)
