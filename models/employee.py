from database.db_manager import get_connection

class Employee:
    def __init__(self, id=None, surname=None, name=None, patronymic=None, phone_number=None):
        self.id = id
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.phone_number = phone_number
        
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id is None:
            cursor.execute("""INSERT INTO employees (surname, name, patronymic, phone_number)
                              VALUES (?, ?, ?, ?)""",
                              (self.surname, self.name, self.patronymic, self.phone_number))
            self.id = cursor.lastrowid
        else:
            cursor.execute("""UPDATE employees SET surname = ?, name = ?, patronymic = ?, 
                              phone_number = ? WHERE id = ?""",
                              (self.surname, self.name, self.patronymic, 
                               self.phone_number, self.id))
        conn.commit()
        conn.close()
        
    def delete(self):
        if self.id is not None:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""DELETE FROM employees WHERE id = ?""",
                           (self.id,))
            conn.commit()
            conn.close()
            
def get_all_employees():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT id, surname, name, patronymic, phone_number FROM employees""")
        rows = cursor.fetchall()
        conn.close()
        return [
            Employee(id=row[0], surname=row[1], name=row[2], 
                   patronymic=row[3], phone_number=row[4])
            for row in rows
        ]
        
def get_employee_by_id(employee_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT id, surname, name, patronymic, phone_number FROM employees
                          WHERE id = ?""",
                          (employee_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Employee(id=row[0], surname=row[1], name=row[2],
                        patronymic=row[3], phone_number=row[4])
        return None