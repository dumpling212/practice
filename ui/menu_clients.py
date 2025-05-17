from models.client import Client, get_all_clients, get_client_by_id

def menu_clients():
    while True:
        print("\n👥=== Управление клиентами ===")
        print("👀 1. Показать всех клиентов")
        print("➕ 2. Добавить клиента")
        print("❌ 3. Удалить клиента")
        print("✏️ 4. Изменить клиента")
        print("🔙 0. Назад в главное меню")
        
        choice = input("👉 Выберите действие: ")
        
        if choice == "1":
            clients = get_all_clients()
            print("\n📋 Список клиентов:")
            for c in clients:
                print(f"👤 {c.id}. {c.surname} {c.name} | 📞 {c.phone_number} | 🏠 {c.address}")
                
        elif choice == "2":
            print("\n➕ Добавление клиента:")
            surname = input("Фамилия: ")
            name = input("Имя: ")
            phone = input("Телефон: ")
            address = input("Адрес: ")
            Client(surname=surname, name=name, phone_number=phone, address=address).save()
            print("✅ Клиент добавлен!")
            
        elif choice == "3":
            client_id = input("Введите ID клиента для удаления: ")
            Client(id=int(client_id)).delete()
            print("🗑️ Клиент удален!")
            
        elif choice == "4":
            client_id = int(input("Введите ID клиента: "))
            client = get_client_by_id(client_id)
            client.surname = input(f"Фамилия [{client.surname}]: ") or client.surname
            client.name = input(f"Имя [{client.name}]: ") or client.name
            client.phone_number = input(f"Телефон [{client.phone_number}]: ") or client.phone_number
            client.address = input(f"Адрес [{client.address}]: ") or client.address
            client.save()
            print("✅ Данные обновлены!")
            
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод!")