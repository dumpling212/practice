from database.db_manager import get_connection

class Client:
    def __init__(self, id=None, surname=None, name=None, patronymic=None, phone_number=None, address=None):
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone_number = phone_number
        self.address = address
        
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""INSERT INTO clients (surname, name, patronymic, phone_number, address)
                              VALUES (?, ?, ?, ?, ?)""",
                              (self.surname, self.name, self.patronymic, self.phone_number, self.address))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""UPDATE clients SET surname = ?, name = ?, patronymic = ?,
                              phone_number = ?, address = ? WHERE id = ?""",
                              (self.surname, self.name, self.patronymic,
                               self.phone_number, self.address, self.id))
        conn.commit()
        conn.close()
        
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM clients WHERE id = ?""",
                           (self.id,))
            conn.commit()
            conn.close()
            
def get_all_clients():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT id, surname, name, patronymic, phone_number, address FROM clients""")
        rows = cursor.fetchall()
        conn.close()
        return [
            Client(id=row[0], surname=row[1], name=row[2], 
                   patronymic=row[3], phone_number=row[4], address=row[5])
            for row in rows
        ]
        
def get_client_by_id(client_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT id, surname, name, patronymic, phone_number, address FROM clients
                          WHERE id = ?""",
                          (client_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Client(id=row[0], surname=row[1], name=row[2],
                        patronymic=row[3], phone_number=row[4], address=row[5])
        return None