menu = {
    'Pizza': 50,
    'Pasta': 90,
    'Burger': 60,
    'Salad': 40,
    'Coffee': 80,
}

print("WELCOME TO SNACKY BICKY RESTAURANT")

print("\nMenu:")
for item, price in menu.items():
    print(f"{item}: {price} INR")

# For cart total
cart_total = 0

# Function to add item to the cart
def add_to_cart(item_name):
    global cart_total
    if item_name in menu:
        cart_total += menu[item_name]
        print(f"Your item '{item_name}' has been added to the order cart.")
    else:
        print(f"Order item '{item_name}' is not available.")

# First item order
item = input("\nWhat would you like to order? ").strip().title()
add_to_cart(item)

# Loop for additional orders
while True:
    more_items = input("Do you want to order anything else? (Yes/No) ").strip().lower()
    if more_items == "yes":
        item = input("Enter the name of the dish you want to order: ").strip().title()
        add_to_cart(item)
    elif more_items == "no":
        break
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

print(f"\nYour cart total is {cart_total} INR.")
