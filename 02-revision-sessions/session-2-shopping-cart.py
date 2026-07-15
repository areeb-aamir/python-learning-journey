cart = []
def add_item(cart, item, price):
    cart.append({"item":item, "price":price})

def remove_item(cart, item):
    for product in cart:
        if product["item"] == item:
            cart.remove(product)
            print(f"{item} remove ho gaya!")
            return
    print(f"{item} cart mein nahi mila!")


def show_cart(cart):
    for product in cart:
        print(f"{product['item']} — Rs. {product['price']}")



def get_total(cart):
    total = 0
    for product in cart:
        total = total + product["price"]
    return total



add_item(cart, "Laptop", 150000)
add_item(cart, "Mouse", 2500)
add_item(cart, "Keyboard", 3500)

show_cart(cart)

remove_item(cart, "Laptop")

print(f"Total: Rs. {get_total(cart)}")

