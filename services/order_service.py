from typing import List, Optional
from sqlalchemy import select
from models.order import Order

# Simple service for order-related database operations
class OrderService:
    def list_orders(self, session, limit: Optional[int] = None) -> List[Order]:
        # Returns a list of all orders, optionally limited
        stmt = select(Order).order_by(Order.id)
        if limit:
            stmt = stmt.limit(limit)
        result = session.execute(stmt).scalars().all()
        return result

    def get_order(self, session, order_id: int) -> Optional[Order]:
        # Looks up a single order by its ID (returns None if not found)
        return session.get(Order, order_id)

    def create_order(self, session, user_id: int) -> Order:
        # Creates a new order for a user
        order = Order(user_id=user_id)
        session.add(order)
        session.flush()  # Assigns an id
        return order

    def update_order(self, session, order_id: int, user_id: Optional[int] = None) -> Order:
        # Updates an existing order's user_id if provided
        order = self.get_order(session, order_id)
        if not order:
            raise ValueError(f"Order {order_id} not found")
        if user_id is not None:
            order.user_id = user_id
        return order

    def delete_order(self, session, order_id: int) -> None:
        # Deletes an order from the database
        order = self.get_order(session, order_id)
        if not order:
            raise ValueError(f"Order {order_id} not found")
        session.delete(order)
