import json

def load_data():
    try:
        with open("business.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"products": {}, "sales": []}

def save_data(data):
    with open("business.json", "w") as f:
        json.dump(data, f)

data = load_data()




def add_item(data, name, price, stock):
    next_id = len(data["products"]) + 1
    data["products"][next_id] = {"Name" : name, "Price" : price, "Stock" : stock}
    save_data(data)
    print("Product Added!")

def update_stock(data, name, stock):
    for id, info in data["products"].items():
        if name == info["Name"]:
            info["Stock"] = int(info["Stock"]) + int(stock)
            save_data(data)
            print("Stock Updated!")
            return
    print("Item Not Found!")


def show_products(data):
    for id, info in data["products"].items():
        print(f"ID : {id}")
        print(f"Name : {info['Name']}")
        print(f"Price : ${info['Price']}")
        print(f"Stock : {info['Stock']}")
        print("     -----     ")

def delete_product(data, name):
    for id, info in data["products"].items():
        if name == info["Name"]:
            del data["products"][id]
            save_data(data)
            print("Data Deleted!")
            return
    print(f"{name}'s Data is Not Exist!")



def record_sale(data, buyer, product_name, quantity):
    for id, info in data["products"].items():
        if product_name == info["Name"]:
            if quantity <= info["Stock"]:
                info["Stock"] = int(info["Stock"]) - int(quantity)
                total_price = int(info["Price"]) * int(quantity)
                data["sales"].append({"Buyer": buyer, "Product": product_name, "Amount": total_price})
                print(f"Your Total Ammount Is : ${total_price}")
                save_data(data)
                return
            elif quantity > info["Stock"]:
                print("We Have Less Stock Now! ")
        elif product_name != info["Name"]:
            print("This Product Is Not Avialable Now!")



def show_reports(data):
    sales = data["sales"]
    products = data["products"]

    total_revenue = sum(i["Amount"] for i in sales)
    print(f"Total Sales revenue : {total_revenue}")
    unique = {p["Buyer"] for p in sales}
    print(f"Unique Buyers Are : {unique}")
    less_stock = [n["Name"] for n in products.values() if n["Stock"] < 5]
    print(f"Less Stock Items Are : {less_stock}")
    totals = {buyer: sum(s["Amount"] for s in sales if s["Buyer"] == buyer)
          for buyer in {s["Buyer"] for s in sales}}
    print(totals)


while True:
    print("======== Your Option ========")
    print("1. Add Product")
    print("2. Update Stock")
    print("3. Show Products")
    print("4. Delete Product")
    print("5. Record Sale")
    print("6. Show Reports")
    print("7. Exit")

    try:
        option = int(input("Option: "))
    except ValueError:
        print("Error - Enter Number!")
        print("     ----     ")
        continue

    if option == 1:
        name = input("Enter Name of Product: ")
        try:
            price = int(input(f"Enter Price of {name}: "))
        except:
            print("Error - Enter Number!")
            print("     ----     ")
            continue
        try:
            stock = int(input("Enter Stock: "))
        except:
            print("Error - Enter Number!")
            print("     ----     ")
            continue
        add_item(data, name, price, stock)


    elif option == 2:
        name = input("Enter Name of Product: ")
        try:
            stock = int(input("Enter Stock: "))
        except:
            print("Error - Enter Number!")
            print("     ----     ")
            continue
        update_stock(data, name, stock)

    elif option == 3:
        show_products(data)
    elif option == 4:
        name = input("Enter Name of Product: ")
        delete_product(data, name)

    elif option == 5:
        buyer = input("Enter Your Name: ")
        product_name = input("Enter Name of Product To Buy: ")
        try:
            quantity = int(input("Enter Stock: "))
        except:
            print("Error - Enter Number!")
            print("     ----     ")
            continue
        record_sale(data, buyer, product_name, quantity)
    elif option == 6:
        show_reports(data)







    elif option == 7:
        print("Bye!")
        break
    else:
        print("Invalid option")




















