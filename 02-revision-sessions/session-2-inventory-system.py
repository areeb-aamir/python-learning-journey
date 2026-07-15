inventory = {}

def add_product(inventory, name, price, stock):
    next_id = len(inventory) + 1
    inventory[next_id] = {"Name": name, "Price" : price, "Stock" : stock}



def update_product(inventory, name, quantity):
    for id, info in inventory.items():
        if info["Name"] == name:
            info["Stock"] = int(info["Stock"]) + int(quantity)
            return
    print("Not Found!")



def low_stock(inventory):
    found_low_stock = False
    for id, info in inventory.items():
        if int(info["Stock"]) < 5:
            print(f"Warning!, You Have Low Stock of {info["Name"]}.")
            found_low_stock = True


    if not found_low_stock:
        print("No Low Stock Found!")





def total_value(inventory):
    total = 0
    for id, info in inventory.items():
        value = int(info["Price"]) * int(info["Stock"])
        total += value
    return total


def show_all(inventory):
    for id, info in inventory.items():
        print(f"ID : {id}")
        print(f"Name : {info['Name']}")
        print(f"Phone Number : {info['Price']}")
        print(f"Stock : {info["Stock"]}")
        print("     -----     ")


