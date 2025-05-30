from database.db_manager import get_connection

class OrderItem:
    def __init__(self, id=None, order_id=None, service_id=None):
        self.id = id
        self.order_id = order_id
        self.service_id = service_id
        
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""INSERT INTO order_items (order_id, service_id)
                              VALUES (?, ?)""",
                              (self.order_id, self.service_id))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""UPDATE order_items SET order_id = ?, service_id = ?
                              WHERE id = ?""",
                              (self.order_id, self.service_id, self.id))
        conn.commit()
        conn.close()
        
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM order_items WHERE id = ?""",
                           (self.id,))
            conn.commit()
            conn.close()
            
def get_all_order_items():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT id, order_id, service_id FROM order_items""")
        rows = cursor.fetchall()
        conn.close()
        return [
            OrderItem(id=row[0], order_id=row[1], service_id=row[2])
            for row in rows
        ]
        
def get_order_item_by_id(item_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT id, order_id, service_id FROM order_items
                          WHERE id = ?""",
                          (item_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return OrderItem(id=row[0], order_id=row[1], service_id=row[2])
        return None

def get_items_by_order_id(order_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT id, order_id, service_id FROM order_items
                          WHERE order_id = ?""",
                          (order_id,))
        rows = cursor.fetchall()
        conn.close()
        return [
            OrderItem(id=row[0], order_id=row[1], service_id=row[2])
            for row in rows
        ]