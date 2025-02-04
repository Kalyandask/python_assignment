import sqlite3

def init_db():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inventory (
            name TEXT PRIMARY KEY,
            quantity INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def add_item(name, quantity):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('INSERT OR REPLACE INTO inventory (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    conn.close()

def remove_item(name):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM inventory WHERE name = ?', (name,))
    conn.commit()
    conn.close()

def update_quantity(name, quantity):
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('UPDATE inventory SET quantity = ? WHERE name = ?', (quantity, name))
    conn.commit()
    conn.close()

def get_inventory():
    conn = sqlite3.connect('inventory.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventory')
    rows = cursor.fetchall()
    conn.close()
    return rows

if __name__ == '__main__':
    init_db()