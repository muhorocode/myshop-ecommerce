from services.order_item_service import OrderItemService
def list_order_items():
    # Lists all order items, optionally filtered by order
    order_id_input = input("Enter order id to filter (leave blank for all): ")
    order_id = int(order_id_input) if order_id_input else None
    with get_session() as session:
        items = OrderItemService().list_order_items(session, order_id)
        for item in items:
            print(f"OrderItem {item.id}: Order {item.order_id}, Product {item.product_id}, Quantity {item.quantity}")

def add_order_item():
    # Adds a product to an order
    try:
        order_id = int(input("Enter order id: "))
        product_id = int(input("Enter product id: "))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid input. Please enter numbers.")
        return
    with get_session() as session:
        try:
            item = OrderItemService().add_order_item(session, order_id, product_id, quantity)
            session.commit()
            print(f"OrderItem added: {item.id} (Order {item.order_id}, Product {item.product_id}, Quantity {item.quantity})")
        except Exception as e:
            print("Error adding order item:", e)

def update_order_item():
    # Updates an order item's product or quantity
    try:
        order_item_id = int(input("Enter order item id to update: "))
    except ValueError:
        print("Invalid order item id.")
        return
    product_id_input = input("Enter new product id (leave blank to keep current): ")
    quantity_input = input("Enter new quantity (leave blank to keep current): ")
    product_id = int(product_id_input) if product_id_input else None
    quantity = int(quantity_input) if quantity_input else None
    with get_session() as session:
        try:
            item = OrderItemService().update_order_item(session, order_item_id, product_id, quantity)
            session.commit()
            print(f"OrderItem updated: {item.id} (Order {item.order_id}, Product {item.product_id}, Quantity {item.quantity})")
        except Exception as e:
            print("Error updating order item:", e)

def delete_order_item():
    # Deletes an order item from the database
    try:
        order_item_id = int(input("Enter order item id to delete: "))
    except ValueError:
        print("Invalid order item id.")
        return
    with get_session() as session:
        try:
            OrderItemService().delete_order_item(session, order_item_id)
            session.commit()
            print("OrderItem deleted.")
        except Exception as e:
            print("Error deleting order item:", e)
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.product_service import ProductService
from services.order_service import OrderService
def list_orders():
    # Lists all orders in the database and prints their details
    with get_session() as session:
        orders = OrderService().list_orders(session)
        for o in orders:
            print(f"{o.id}: User {o.user_id} - Created at {o.created_at}")

def create_order():
    # Adds a new order for a user
    try:
        user_id = int(input("Enter user id for the order: "))
    except ValueError:
        print("Invalid user id.")
        return
    with get_session() as session:
        try:
            order = OrderService().create_order(session, user_id)
            session.commit()
            print(f"Order created: {order.id} for user {order.user_id}")
        except Exception as e:
            print("Error creating order:", e)

def update_order():
    # Updates an existing order's user_id
    try:
        order_id = int(input("Enter order id to update: "))
    except ValueError:
        print("Invalid order id.")
        return
    user_id_input = input("Enter new user id (leave blank to keep current): ")
    user_id = int(user_id_input) if user_id_input else None
    with get_session() as session:
        try:
            order = OrderService().update_order(session, order_id, user_id)
            session.commit()
            print(f"Order updated: {order.id} for user {order.user_id}")
        except Exception as e:
            print("Error updating order:", e)

def delete_order():
    # Deletes an order from the database
    try:
        order_id = int(input("Enter order id to delete: "))
    except ValueError:
        print("Invalid order id.")
        return
    with get_session() as session:
        try:
            OrderService().delete_order(session, order_id)
            session.commit()
            print("Order deleted.")
        except Exception as e:
            print("Error deleting order:", e)
from services.user_service import UserService
def list_users():
    # Lists all users in the database and prints their details
    with get_session() as session:
        users = UserService().list_users(session)
        for u in users:
            print(f"{u.id}: {u.username} - {u.email}")

def create_user():
    # Adds a new user to the database
    username = input("Enter username: ")
    email = input("Enter email: ")
    with get_session() as session:
        try:
            user = UserService().create_user(session, username, email)
            session.commit()
            print(f"User created: {user.id}: {user.username}")
        except Exception as e:
            print("Error creating user:", e)

def update_user():
    # Updates an existing user's details
    try:
        user_id = int(input("Enter user id to update: "))
    except ValueError:
        print("Invalid user id.")
        return
    username = input("Enter new username (leave blank to keep current): ")
    email = input("Enter new email (leave blank to keep current): ")
    with get_session() as session:
        try:
            user = UserService().update_user(session, user_id, username or None, email or None)
            session.commit()
            print(f"User updated: {user.id}: {user.username}")
        except Exception as e:
            print("Error updating user:", e)

def delete_user():
    # Deletes a user from the database
    try:
        user_id = int(input("Enter user id to delete: "))
    except ValueError:
        print("Invalid user id.")
        return
    with get_session() as session:
        try:
            UserService().delete_user(session, user_id)
            session.commit()
            print("User deleted.")
        except Exception as e:
            print("Error deleting user:", e)
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
        print("6. List all users")
        print("7. Add a new user")
        print("8. Update a user")
        print("9. Delete a user")
        print("10. List all orders")
        print("11. Add a new order")
        print("12. Update an order")
        print("13. Delete an order")
        print("14. List order items")
        print("15. Add order item")
        print("16. Update order item")
        print("17. Delete order item")
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
        elif choice == "6":
            list_users()
        elif choice == "7":
            create_user()
        elif choice == "8":
            update_user()
        elif choice == "9":
            delete_user()
        elif choice == "10":
            list_orders()
        elif choice == "11":
            create_order()
        elif choice == "12":
            update_order()
        elif choice == "13":
            delete_order()
        elif choice == "14":
            list_order_items()
        elif choice == "15":
            add_order_item()
        elif choice == "16":
            update_order_item()
        elif choice == "17":
            delete_order_item()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    # Start the CLI application by showing the main menu
    main_menu()