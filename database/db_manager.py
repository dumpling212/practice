import sqlite3
from config import DB_NAME

def get_connection():
    return sqlite3.connect(DB_NAME)

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS services (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT NOT NULL,
                      price REAL NOT NULL,
                      category_id INTEGER NOT NULL,
                      FOREIGN KEY (category_id) REFERENCES categories(id))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS clients (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      surname TEXT NOT NULL,
                      name TEXT NOT NULL,
                      patronymic TEXT,
                      phone_number INTEGER NOT NULL,
                      address STRING NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS employees (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      surname TEXT NOT NULL,
                      name TEXT NOT NULL,
                      patronymic TEXT,
                      phone_number INTEGER NOT NULL)''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      order_date DATE NOT NULL,
                      client_id INTEGER,
                      employee_id INTEGER,
                      total_amount REAL NOT NULL,
                      FOREIGN KEY (client_id) REFERENCES clients(id),
                      FOREIGN KEY (employee_id) REFERENCES employees(id))''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS order_items (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      order_id INTEGER,
                      service_id INTEGER,
                      FOREIGN KEY (order_id) REFERENCES orders(id),
                      FOREIGN KEY (service_id) REFERENCES service(id))''')
    
    conn.commit()
    conn.close()