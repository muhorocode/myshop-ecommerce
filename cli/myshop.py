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
            print(f"{p.id}: {p.name} - ${p.price} (Stock: {p.stock_quantity})")

def create_product():
    # Adds a new product to the database
    name = input("Enter product name: ")
    try:
        price = float(input("Enter product price: "))
        stock = int(input("Enter stock quantity: "))
    except ValueError:
        print("Invalid price or stock quantity. Please enter numbers.")
        return
    with get_session() as session:
        try:
            product = ProductService().create_product(session, name, price, stock)
            session.commit()
            print(f"Product created: {product.id}: {product.name}")
        except Exception as e:
            print("Error creating product:", e)

def update_product():
    # Updates an existing product's details
    try:
        product_id = int(input("Enter product id to update: "))
    except ValueError:
        print("Invalid product id.")
        return
    name = input("Enter new name (leave blank to keep current): ")
    price_input = input("Enter new price (leave blank to keep current): ")
    stock_input = input("Enter new stock quantity (leave blank to keep current): ")
    price = float(price_input) if price_input else None
    stock = int(stock_input) if stock_input else None
    with get_session() as session:
        try:
            product = ProductService().update_product(session, product_id, name or None, price, stock)
            session.commit()
            print(f"Product updated: {product.id}: {product.name}")
        except Exception as e:
            print("Error updating product:", e)

def delete_product():
    # Deletes a product from the database
    try:
        product_id = int(input("Enter product id to delete: "))
    except ValueError:
        print("Invalid product id.")
        return
    with get_session() as session:
        try:
            ProductService().delete_product(session, product_id)
            session.commit()
            print("Product deleted.")
        except Exception as e:
            print("Error deleting product:", e)

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
        print("3. Add a new product")
        print("4. Update a product")
        print("5. Delete a product")
        print("0. Exit")
        choice = input("> ")  # Get the user's menu choice
        if choice == "1":
            list_products()
        elif choice == "2":
            show_product()
        elif choice == "3":
            create_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    # Start the CLI application by showing the main menu
    main_menu()