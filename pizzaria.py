#W5 SE126 

#Braedin Yarletts
#Lab #5 
#August 19th


#VARIBLE DICTIONARY
#---------------------------------------------------------------------------------------------------------
#price_width: Represents the maximum width for the price column in the menu and receipt. It ensures proper alignment of prices.
#quantity_width: Represents the maximum width for the quantity column in the receipt. It ensures proper alignment of quantities.
#item_total:  Represents the total cost for a specific item (price multiplied by quantity). It is used to compute the total cost for each item in the receipt.
#filename: Name of the CSV file.
#menu: Dictionary of menu items and prices.
#file: File object for reading.
#reader: CSV reader object.
#line: Row from the CSV file.
#item: Menu item name.
#price: Price of a menu item.
#order: Dictionary of ordered items and quantities.
#quantity: Number of units ordered.
#---------FUNCTIONS---------------------------------------------------------------------------------------

import csv

def load_menu():
    filename = 'pizza.csv'  # Hardcoded CSV filename
    menu = {}
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for line in reader:
            if len(line) != 2:
                print(f"Skipping malformed line: {line}")
                continue
            item, price = line
            try:
                menu[item] = float(price)
            except ValueError:
                print(f"Skipping invalid price '{price}' for item '{item}'")
    return menu

# Print the menu with item names and prices
def print_menu(menu):
    print("Welcome to the Pizzeria!")
    print("Here is our menu:")
    
    item_width = 0
    price_width = 0
    
    # Determine the maximum width required for item names and prices
    for item in menu:
        item_width = max(item_width, len(item))
        price_width = max(price_width, len(f"${menu[item]:.2f}"))

    item_width += 2
    price_width += 2
    
    print(f"{'Item':<{item_width}} {'Price':>{price_width}}")
    print('-' * (item_width + price_width))
    
    for item in menu:
        print(f"{item:<{item_width}} ${menu[item]:>{price_width}.2f}")
    print()


def take_order(menu):
    order = {}
    while True:
        print("-----------------------------------------------------")
        item = input("Enter the pizza you want to order (or type 'done' to finish): ")
        if item.lower() == 'done':
            if order:
                return order
            else:
                print("You haven't ordered anything yet. Please order at least one item.")
                continue
        if item not in menu:
            print("Sorry, we don't have that item. Please choose from the menu.")
            continue
        quantity = input(f"How many of {item}'s would you like? ")
        try:
            quantity = int(quantity)
            if quantity <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid number. Please enter a valid quantity.")
            continue
        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity


def print_receipt(order, menu):
    print("\n--- Receipt ---")
    
    item_width = 0
    quantity_width = 0
    price_width = 0
    
    
    for item in order:
        item_width = max(item_width, len(item))
        quantity_width = max(quantity_width, len(f"x{order[item]}"))
        price_width = max(price_width, len(f"${menu[item] * order[item]:.2f}"))

    item_width += 2
    quantity_width += 2
    price_width += 2
    
    print(f"{'Item':<{item_width}} {'Quantity':<{quantity_width}} {'Total':>{price_width}}")
    print('-' * (item_width + quantity_width + price_width))
    
    total = 0
    for item in order:
        item_total = menu[item] * order[item]
        total += item_total
        print(f"{item:<{item_width}} x{order[item]:<{quantity_width}} ${item_total:>{price_width}.2f}")
    print(f"{'Total amount due:':<{item_width + quantity_width}} ${total:>{price_width}.2f}")

def main():
    menu = load_menu()
    if menu:
        print_menu(menu)
        order = take_order(menu)
        if order:
            print_receipt(order, menu)
        else:
            print("No items ordered.")
    else:
        print("Menu could not be loaded. Please check the CSV file.")

if __name__ == "__main__":
    main()
