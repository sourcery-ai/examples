import sqlite3
from datetime import datetime

# Database connection setup
conn = sqlite3.connect('enterprise_inventory.db')
cursor = conn.cursor()

# Ensure that the needed table exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    product_id INTEGER PRIMARY KEY,
    product_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    last_updated TIMESTAMP NOT NULL
)
''')
conn.commit()

# A class to represent the inventory
class Inventory:
    def __init__(self):
        self._products = self._load_products()

    def _load_products(self):
        cursor.execute("SELECT * FROM inventory")
        return {row[0]: {'product_name': row[1], 'quantity': row[2], 'last_updated': row[3]} for row in cursor.fetchall()}

    def add_product(self, product_name, quantity):
        if not isinstance(product_name, str) or not isinstance(quantity, int):
            raise ValueError("Invalid input types for product name or quantity.")

        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        now = datetime.now()
        cursor.execute("INSERT INTO inventory (product_name, quantity, last_updated) VALUES (?, ?, ?)",
                       (product_name, quantity, now))
        conn.commit()
        self._products[cursor.lastrowid] = {'product_name': product_name, 'quantity': quantity, 'last_updated': now}

    def remove_product(self, product_id):
        if product_id not in self._products:
            raise ValueError("Product ID does not exist in inventory.")
        
        cursor.execute("DELETE FROM inventory WHERE product_id = ?", (product_id,))
        conn.commit()
        del self._products[product_id]

    def update_quantity(self, product_id, quantity_change):
        if product_id not in self._products:
            raise ValueError("Product ID does not exist in inventory.")
        
        new_quantity = self._products[product_id]['quantity'] + quantity_change
        if new_quantity < 0:
            raise ValueError("Cannot have negative quantity in inventory.")

        now = datetime.now()
        cursor.execute("UPDATE inventory SET quantity = ?, last_updated = ? WHERE product_id = ?",
                       (new_quantity, now, product_id))
        conn.commit()
        self._products[product_id].update({'quantity': new_quantity, 'last_updated': now})

    def get_product_info(self, product_id):
        return self._products.get(product_id)

    def __del__(self):
        conn.close()

def main():
    inventory = Inventory()
    
    # Add a few products
    inventory.add_product('Laptop', 10)
    inventory.add_product('Mouse', 50)
    inventory.add_product('Keyboard', 20)

    # Remove a product
    inventory.remove_product(2)

    # Update quantity
    inventory.update_quantity(1, -2)

    # Print information about a product
    print(inventory.get_product_info(1))

if __name__ == "__main__":
    main()
