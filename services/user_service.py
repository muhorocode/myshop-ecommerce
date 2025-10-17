from typing import List, Optional
from sqlalchemy import select
from models.user import User

# Simple service for user-related database operations
class UserService:
	def list_users(self, session, limit: Optional[int] = None) -> List[User]:
		# Returns a list of all users, optionally limited
		stmt = select(User).order_by(User.id)
		if limit:
			stmt = stmt.limit(limit)
		result = session.execute(stmt).scalars().all()
		return result

	def get_user(self, session, user_id: int) -> Optional[User]:
		# Looks up a single user by their ID (returns None if not found)
		return session.get(User, user_id)

	def create_user(self, session, username: str, email: str) -> User:
		# Creates a new user and adds them to the database
		if not username or not email:
			raise ValueError("Username and email are required")
		user = User(username=username, email=email)
		session.add(user)
		session.flush()  # Assigns an id
		return user

	def update_user(self, session, user_id: int, username: Optional[str] = None, email: Optional[str] = None) -> User:
		# Updates an existing user's username and/or email
		user = self.get_user(session, user_id)
		if not user:
			raise ValueError(f"User {user_id} not found")
		if username is not None:
			user.username = username
		if email is not None:
			user.email = email
		return user

	def delete_user(self, session, user_id: int) -> None:
		# Deletes a user from the database
		user = self.get_user(session, user_id)
		if not user:
			raise ValueError(f"User {user_id} not found")
		session.delete(user)
