import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.product_service import ProductService
from db.connection import get_session

def list_products():
    # Lists all products in the database and prints their details
    with get_session() as session:
        products = ProductService().list_products(session)
        for p in products:
            # Print each product's id, name, price, and stock
            print(f"{p.id}: {p.name} - ${p.price} (Stock: {p.stock_quantity})")

def show_product():
    # Shows details for a single product by its ID
    product_id = input("Enter product id: ")  # Ask the user for the product id
    with get_session() as session:
        # Try to get the product from the database
        product = ProductService().get_product(session, int(product_id))
        if product:
            # Print product details if found
            print(f"{product.id}: {product.name} - ${product.price} (Stock: {product.stock_quantity})")
        else:
            # Inform the user if the product does not exist
            print("Product not found.")

def main_menu():
    # Main menu loop for the CLI
    while True:
        # Print the available options for the user
        print("\nPlease select an option:")
        print("1. List all products")
        print("2. Show product details")
        print("0. Exit")
        choice = input("> ")  # Get the user's menu choice
        if choice == "1":
            # Call the function to list all products
            list_products()
        elif choice == "2":
            # Call the function to show a single product's details
            show_product()
        elif choice == "0":
            # Exit the program
            print("Goodbye!")
            break
        else:
            # Handle invalid menu choices
            print("Invalid option. Try again.")

if __name__ == "__main__":
    # Start the CLI application by showing the main menu
    main_menu()