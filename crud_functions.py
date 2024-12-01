import sqlite3


def initiate_db():

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def add_product(title, description, price):

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Products (title, description, price) VALUES (?, ?, ?)', (title, description, price))
    conn.commit()
    conn.close()


def get_all_products():

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products


if __name__ == "__main__":
    initiate_db()
    add_product("Product1", "APPLE", 100)
    add_product("Product2", "lemon", 200)
    add_product("Product3", "orange", 300)
    add_product("Product4", "pear", 400)