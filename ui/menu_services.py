from models.service import Service, get_all_services, get_service_by_id
from models.category import get_all_categories
import sqlite3

def menu_services():
    while True:
        print("\n🔧=== Управление услугами ===")
        print("👀 1. Показать все услуги")
        print("➕ 2. Добавить услугу")
        print("❌ 3. Удалить услугу")
        print("✏️ 4. Изменить услугу")
        print("🔙 0. Назад в главное меню")
        
        choice = input("👉 Выберите действие: ")
        
        if choice == "1":
            services = get_all_services()
            print("\n📋 Список услуг:")
            for s in services:
                print(f"🆔 {s.id}. {s.title} | 💰 Цена: {s.price} руб. | 🏷 Категория ID: {s.category_id}")
                
        elif choice == "2":
            print("\n➕ Добавление новой услуги")
            title = input("Название услуги: ")
            price = float(input("Цена: "))
            
            print("\n🏷 Доступные категории:")
            categories = get_all_categories()
            for c in categories:
                print(f"{c.id} - {c.title}")
            category_id = int(input("Введите ID категории: "))
            
            service = Service(title=title, price=price, category_id=category_id)
            service.save()
            print("✅ Услуга добавлена!")
            
        elif choice == "3":
            service_id = input("Введите ID услуги для удаления: ")
    
            service_id_int = int(service_id)
            affected_rows = Service(id=service_id_int).delete()
        
            if affected_rows > 0:
                print("🗑️ Услуга удалена!")
            else:
                print("⚠️ Услуга с таким ID не найдена!")
            
            
        elif choice == "4":
            service_id = int(input("Введите ID услуги для редактирования: "))
            service = get_service_by_id(service_id)
            
            print("\n✏️ Редактирование услуги:")
            title = input(f"Название [{service.title}]: ") or service.title
            price = input(f"Цена [{service.price}]: ") or service.price
            
            service.title = title
            service.price = float(price)
            service.save()
            print("✅ Услуга обновлена!")
            
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод!")