# =================== WELCOME AND SETUP===============================

INVENTORY_FILE = "Dictionary.txt"
SALES_FILE = "sales_log.txt"
SOLD_PRODUCTS_FILE = "sold_products.txt"

# Function to get owner's info
def ask_kiosk_info():
    kiosk_name = input('Enter the Kiosk name: ').strip().title()
    owner_name = input('Enter the name of the owner: ').strip().title()
    return kiosk_name,owner_name


# Function to print kiosk details
def show_owner_details(kiosk_name,owner_name):
    print(f"Welcome to {kiosk_name}'s Kiosk Manager, run by {owner_name}")

# gets and upacks the returned value
kiosk_name , owner_name = ask_kiosk_info()

# Pass the value to the next function
show_owner_details(kiosk_name,owner_name)

print()  #Prints an empty line so that our work in the terminal can be presentable

# Creating an inventory
inventory = {
    "Pen": {"price": 65, "quantity": 20},
    "Books": {"price": 80, "quantity": 15},
    "Print papers": {"price": 160,"quantity": 10}
}

# function to save an inventory
def save_inventory():
    with open(INVENTORY_FILE, 'w') as f:
        for product, details in inventory.items():
            f.write(
                f"{product},{details['price']},{details['quantity']}\n")
    print('Inventory saved successfully')

sales_log = []
sold_products = set()

# Function to save sales sold
def save_sales_log():
    with open(SALES_FILE, "w") as file:
        for sale in sales_log:
            product, quantity, total = sale

            file.write(f"{product},{quantity},{total}\n")

# Function to save unique products
def save_sold_products():
    with open(SOLD_PRODUCTS_FILE, "w") as file:
        for product in sold_products:
            file.write(f"{product}\n")


#=========================== function to view stock===================
def view_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            print("\nINVENTORY")
            print("-" * 40)
            print(f"{'Product':<15}{'Price':<12}{'Quantity':<10}")
            print("-" * 40)

            for line in file:
                product, price, quantity = line.strip().split(",")

                print(f"{product:<15}{price:<12}{quantity:<10}")

    except FileNotFoundError:
        print("Inventory file does not exist yet.")

# ================function to add/ restock a product========================
def add_or_restock_product():

    product = input("Enter product name: ").strip().title()

    # Validate product name
    if product == "" or product.isdigit():
        print("Invalid product name. Please enter a valid product name.")
        return

    # Product already exists
    if product in inventory:

        quantity = input("Enter quantity to add: ").strip()

        if not quantity.isdigit():
            print("Quantity must be a number.")
            return

        quantity = int(quantity)

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            return

        inventory[product]["quantity"] += quantity

        save_inventory()

        print(f"{product} has been restocked successfully.")

    # Brand-new product
    else:

        price = input("Enter product price: ").strip()
        quantity = input("Enter product quantity: ").strip()

        if not price.isdigit() or not quantity.isdigit():
            print("Price and quantity must be numbers.")
            return

        price = int(price)
        quantity = int(quantity)

        if price <= 0 or quantity <= 0:
            print("Price and quantity must be greater than 0.")
            return

        inventory[product] = {
            "price": price,
            "quantity": quantity
        }

        save_inventory()

        print(f"{product} has been added successfully.")

#=============== Function to Sell a Product================
def sell_product():
    product = input('Which product to sell: ').strip().title()

    # Validate product name
    if product == "" or product.isdigit():
        print("Invalid product name. Please enter a valid product name.")
        return
    if product not in inventory:
        print(f"{product} is not available in the inventory.")
        return
    
    if product in inventory:
        quantity = input('Enter the units to be sold: ').strip()

        if not quantity.isdigit():
            print('Quantity must be a digit')
            return
        quantity = int(quantity)

        if quantity <= 0:
            print('Quantity should be greater than 0')
            return

        if quantity > inventory[product]["quantity"]:
            print(
            f"Not enough stock. Only "
            f"{inventory[product]['quantity']} units available.")
            return

        price = inventory[product]['price']
        total = quantity * price

        inventory[product]["quantity"] -= quantity

        sale = (product, quantity, total)

        sales_log.append(sale)

        sold_products.add(product)
        
        save_inventory()
        save_sales_log()
        save_sold_products()

        print(f"Sold {quantity} units of {product} sucessfuly for {total}")

    print("Sale successful.")
    print(f"Product: {product}")
    print(f"Quantity: {quantity}")
    print(f"Total: KES {total}")


#===============Function to print the sales report==============================

def sales_report():
    if not sales_log:
        print("No sales yet this session.")
        return

    print("\nSALES REPORT")
    print("-" * 40)
    print(f"{'Product':<15}{'Quantity':<10}{'Total (KES)':<12}")
    print("-" * 40)

    revenue = 0
    units_by_product = {}
    for product, quantity, total in sales_log:
        print(f"{product:<15}{quantity:<10}{total:<12}")
        revenue += total
        units_by_product[product] = units_by_product.get(product, 0) + quantity

    best = max(units_by_product, key=units_by_product.get)
    print("-" * 40)
    print(f"Total revenue: KES {revenue}")
    print(f"Unique products sold: {len(sold_products)}")
    print(f"Best seller: {best} ({units_by_product[best]} units)\n")


# ===============Function to search products====================
def search_products():
    term = input("Search for a product: ").strip().lower()
    if term == "":
        print("Please type something to search for.")
        return

    found = False
    for product, details in inventory.items():
        if term in product.lower():
            print(f"{product:<15}KES {details['price']:<8}Qty: {details['quantity']}")
            found = True
    if not found:
        print("No matches found.")

# Main menu Loop
while True:
    print('==============MAIN MENU============== ')
    print('1. View Stock')
    print('2. Add/ Restock a Product')
    print('3. Sell a Product')
    print('4. View Sales Report')
    print('5. Search Products')
    print('6. Exit')

    choice = input('Enter your choice(Between 1 and 6): ')

    if not choice.isdigit():
        print('Invalid choice. Please enter a number between 1 and 6')
        continue

    choice = int(choice)


    if choice < 1 or choice > 6 :
        print('Invalid choice. please neter a number between 1 and 6')
        continue

    if choice == 1 :
        view_inventory()
    elif choice == 2 :
        add_or_restock_product()
    elif choice == 3 :
        sell_product()
    elif choice == 4 :
        sales_report()
    elif choice == 5 :
        search_products()
    else:
        print('Exiting, Goodbye!!!!')
        break




