from products import Product
from store import Store


def list_all_products(store: Store):
    """Lists all active products in the store with a numbered format."""
    active_products = store.get_all_products()
    if active_products:
        print("------")
        for i, product in enumerate(active_products, start=1):
            print(f"{i}. {product.name}, Price: ${product.price}, Quantity: {product.get_quantity()}")
        print("------")
    else:
        print("No active products in the store.")


def show_total_quantity(store: Store):
    """Shows the total quantity of all active products in the store."""
    total_quantity = store.get_total_quantity()
    print(f"Total of {total_quantity} items in store")


def make_order(store: Store):
    """Allows the user to make an order."""
    shopping_list = []
    list_all_products(store)
    print("When you want to finish order, enter empty text.")
    while True:
        # Get the product selection from the user
        product_choice = input("Which product # do you want?): ")
        if product_choice == "":
            break

        # Ensure the choice is valid
        try:
            product_index = int(product_choice) - 1
            active_products = store.get_all_products()
            if 0 <= product_index < len(active_products):
                selected_product = active_products[product_index]
                quantity = int(input(f"What amount do you want?"))
                if quantity <= 0 or quantity > selected_product.get_quantity():
                    print(f"Invalid quantity. Please enter a value between 1 and {selected_product.get_quantity()}.")
                else:
                    shopping_list.append((selected_product, quantity))
                    print("Product added to list!")
                    # Do not print the product list again after adding to the list
            else:
                print("Invalid product number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

    if shopping_list:
        try:
            total_cost = store.order(shopping_list)
            print(f"Order total cost: {total_cost} dollars.")
        except ValueError as e:
            print(e)
    else:
        print("No items added to the order.")



def start(store: Store):
    """Shows the user interface menu and allows interaction."""
    while True:
        print("\n    Store Menu")
        print("    ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == '1':
            list_all_products(store)
        elif choice == '2':
            show_total_quantity(store)
        elif choice == '3':
            make_order(store)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option (1-4).")


# Setup initial inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]

# Create a store object with the initial products
best_buy = Store(product_list)

# Start the user interface
start(best_buy)
