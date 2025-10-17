from typing import List, Optional
from sqlalchemy import select
from models.product import Product

# simple service for product related db operations
class ProductService:
    def list_products(self, session, limit: Optional[int] = None) -> List[Product]:
        # Creates a query to select all products from the database, ordered by their ID
        stmt = select(Product).order_by(Product.id)
        # If a limit is given, only that number of products will be returned (useful for previews)
        if limit:
            stmt = stmt.limit(limit)
        # Runs the query and gets all product objects as a list
        result = session.execute(stmt).scalars().all()
        return result

    def get_product(self, session, product_id: int) -> Optional[Product]:
        # Looks up a single product by its ID (returns None if not found)
        return session.get(Product, product_id)

    def reduce_stock(self, session, product_id: int, quantity: int) -> None:
        # Makes sure the quantity to reduce is a positive number
        if quantity <= 0:
            raise ValueError("quantity must be greater than 0")
        # Gets the product by ID (or raises an error if not found)
        product = self.get_product(session, product_id)
        if product is None:
            raise ValueError(f"Product {product_id} not found")
        # Checks if there is enough stock to reduce by the requested amount
        if product.stock_quantity < quantity:
            raise ValueError(f"Not enough stock for product {product_id}")
        # Subtracts the quantity from the product's stock
        product.stock_quantity -= quantity


