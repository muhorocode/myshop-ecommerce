from typing import List, Optional
from sqlalchemy import select
from models.order_item import OrderItem

# Simple service for order item-related database operations
class OrderItemService:
    def list_order_items(self, session, order_id: Optional[int] = None) -> List[OrderItem]:
        # Returns a list of all order items, optionally filtered by order_id
        stmt = select(OrderItem).order_by(OrderItem.id)
        if order_id:
            stmt = stmt.where(OrderItem.order_id == order_id)
        result = session.execute(stmt).scalars().all()
        return result

    def get_order_item(self, session, order_item_id: int) -> Optional[OrderItem]:
        # Looks up a single order item by its ID (returns None if not found)
        return session.get(OrderItem, order_item_id)

    def add_order_item(self, session, order_id: int, product_id: int, quantity: int) -> OrderItem:
        # Adds a product to an order with the specified quantity
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
        order_item = OrderItem(order_id=order_id, product_id=product_id, quantity=quantity)
        session.add(order_item)
        session.flush()  # Assigns an id
        return order_item

    def update_order_item(self, session, order_item_id: int, product_id: Optional[int] = None, quantity: Optional[int] = None) -> OrderItem:
        # Updates an existing order item's product or quantity
        order_item = self.get_order_item(session, order_item_id)
        if not order_item:
            raise ValueError(f"OrderItem {order_item_id} not found")
        if product_id is not None:
            order_item.product_id = product_id
        if quantity is not None:
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero")
            order_item.quantity = quantity
        return order_item

    def delete_order_item(self, session, order_item_id: int) -> None:
        # Deletes an order item from the database
        order_item = self.get_order_item(session, order_item_id)
        if not order_item:
            raise ValueError(f"OrderItem {order_item_id} not found")
        session.delete(order_item)
