from database.db_manager import get_connection

class Service:
    def __init__(self, id=None, title=None, price=None, category_id=None): 
        self.id = id
        self.title = title
        self.price = price
        self.category_id = category_id
        
    def save(self): 
        conn = get_connection() 
        cursor = conn.cursor() 
        if self.id is None: 
            cursor.execute("""INSERT INTO services (title, price, category_id)
                              VALUES (?, ?, ?)""",
                              (self.title, self.price, self.category_id))
            self.id = cursor.lastrowid 
        else: 
            cursor.execute("""UPDATE services SET title = ?, price = ?, category_id = ?
                              WHERE id = ? """,
                              (self.title, self.price, self.category_id, self.id))
        conn.commit()
        conn.close()
        
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM services WHERE id = ?""",
                           (self.id))
            conn.commit()
            conn.close()
            
def get_all_services(): 
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute("""SELECT id, title, price, category_id FROM products""") 
        rows = cursor.fetchall() 
        conn.close() 
        return [ 
            Service(id=row[0], title=row[1], price=row[2], category_id=row[3],
            )
            for row in rows
        ]
def get_service_by_id(service_id):
        conn = get_connection() 
        cursor = conn.cursor() 
        cursor.execute("""SELECT id, title, price, category_id FROM products
                      WHERE id = ?""",
                      (service_id))
        row = cursor.fetchone() 
        conn.close() 
        if row: 
            return Service(id=row[0], title=row[1], price=row[3], category_id=row[5]
        ) 
        return None