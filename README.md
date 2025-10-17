# MyShop E-commerce Backend

A simple, beginner-friendly e-commerce backend built with Python, PostgreSQL, SQLAlchemy, and a command-line interface (CLI). This project demonstrates CRUD operations, database relationships, and a clean git workflow. Designed for learning and easy understanding—even for non-coders!

---

## Features
- Manage Products: Add, update, list, and delete products
- Manage Users: Add, update, list, and delete users
- Manage Orders: Create, update, list, and delete orders
- Manage Order Items: Add products to orders, update, list, and delete order items
- All operations available via a simple CLI
- Automated tests for all services (pytest)

---

## Tech Stack
- **Python 3**
- **PostgreSQL** (database)
- **SQLAlchemy** (ORM)
- **psycopg2** (PostgreSQL driver)
- **pytest** (testing)
- **Git** (feature branch workflow)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/muhorocode/myshop-ecommerce.git
cd myshop-ecommerce
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up PostgreSQL Database
- Create a PostgreSQL database (e.g., `myshop_db`)
- Update your database connection string in `db/connection.py` if needed

### 4. Initialize the Database
- Run the setup script to create tables:
```bash
python db/setup.py
```

### 5. Run the CLI
From the project root:
```bash
python -m cli.myshop
```

### 6. Run the Tests
From the project root:
```bash
PYTHONPATH=. pytest -q
```

---

## Example Usage
- List all products
- Add a new user
- Create an order for a user
- Add products to an order
- Delete a user (must delete their orders first)
- Run automated tests to verify all services

All actions are menu-driven and beginner-friendly!

---

## Project Structure
```
myshop-ecommerce/
├── cli/                # Command-line interface
├── db/                 # Database connection and setup
├── models/             # SQLAlchemy models
├── services/           # Business logic (CRUD services)
├── tests/              # Automated tests (pytest)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

---

## Author
- GitHub: [muhorocode](https://github.com/muhorocode)
- (You can add your real name if you wish, or just use your GitHub handle for privacy.)

---

## License
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## Notes
- For learning/demo purposes. Not production-ready.
- To delete a user, you must first delete all their orders (database safety).
- For questions or contributions, open an issue or pull request!
