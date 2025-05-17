from database.db_manager import get_connection

class Order: 
    def __init__(self, id=None, order_date=None, client_id=None, employee_id=None, total_amount=0.0):
        self.id = id
        self.order_date = order_date
        self.client_id = client_id
        self.employee_id = employee_id
        self.total_amount = total_amount
        
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""INSERT INTO orders (order_date, client_id, employee_id, total_amount)
                              VALUES (?, ?, ?, ?)""",
                              (self.order_date, self.client_id, self.employee_id, self.total_amount)
                          )
            self.id = cursor.lastrowid
        else: 
            cursor.execute("""UPDATE orders SET order_date = ?, client_id = ?, employee_id = ?, total_amount = ?
                              WHERE id = ?""",
                              (self.order_date, self.client_id, self.employee_id, self.total_amount, self.id)
                          )
        conn.commit()
        conn.close()
        
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM orders WHERE id = ?""",
                              (self.id))
        conn.commit()
        conn.close()
        
def get_all_orders():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT id, order_date, client_id, employee_id, total_amount FROM orders""")
        rows = cursor.fetchall()
        conn.close()
        return [Order(id=row[0], order_date=row[1], client_id=row[2], employee_id=row[3], total_amount=row[4]) for row in rows]
    
def get_order_by_id(order_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT id, order_date, client_id, employee_id, total_amount FROM orders WHERE id = ?""",
                          (order_id))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Order(id=row[0], order_date=row[1], client_id=row[2], employee_id=row[3], total_amount=row[4])
        return None