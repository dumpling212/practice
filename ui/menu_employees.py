from models.employee import Employee, get_all_employees, get_employee_by_id

def menu_employees():
    while True:
        print("\n👨‍💼=== Управление сотрудниками ===")
        print("👀 1. Показать всех сотрудников")
        print("➕ 2. Добавить сотрудника")
        print("❌ 3. Удалить сотрудника")
        print("✏️ 4. Изменить сотрудника")
        print("🔙 0. Назад в главное меню")
        
        choice = input("👉 Выберите действие: ")
        
        if choice == "1":
            employees = get_all_employees()
            print("\n📋 Список сотрудников:")
            for e in employees:
                print(f"👔 {e.id}. {e.surname} {e.name} | 📞 {e.phone_number}")
                
        elif choice == "2":
            print("\n➕ Добавление сотрудника:")
            surname = input("Фамилия: ")
            name = input("Имя: ")
            phone = input("Телефон: ")
            Employee(surname=surname, name=name, phone_number=phone).save()
            print("✅ Сотрудник добавлен!")
            
        elif choice == "3":
            emp_id = input("Введите ID сотрудника для удаления: ")
            Employee(id=int(emp_id)).delete()
            print("🗑️ Сотрудник удален!")
            
        elif choice == "4":
            emp_id = int(input("Введите ID сотрудника: "))
            emp = get_employee_by_id(emp_id)
            emp.surname = input(f"Фамилия [{emp.surname}]: ") or emp.surname
            emp.name = input(f"Имя [{emp.name}]: ") or emp.name
            emp.phone_number = input(f"Телефон [{emp.phone_number}]: ") or emp.phone_number
            emp.save()
            print("✅ Данные обновлены!")
            
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод!")