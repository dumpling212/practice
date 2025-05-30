from models.order import Order, get_all_orders, get_order_by_id
from models.client import get_all_clients, get_client_by_id
from models.employee import get_all_employees
from models.service import get_all_services, get_service_by_id
from models.order_item import OrderItem, get_items_by_order_id
from datetime import datetime

def manage_order_items(order_id):
    while True:
        order = get_order_by_id(order_id)
        client = get_client_by_id(order.client_id)
        
        print(f"\n📦=== Позиции заказа #{order_id} ===")
        print(f"👤 Клиент: {client.surname} {client.name}")
        print(f"📅 Дата: {order.order_date}")
        print("--------------------------------")
        
        items = get_items_by_order_id(order_id)
        total = 0
        
        if not items:
            print("ℹ️ Нет добавленных услуг")
        else:
            print("🔹 Список услуг в заказе:")
            for item in items:
                service = get_service_by_id(item.service_id)
                print(f"  🆔 {item.id}. {service.title} | 💰 {service.price} руб.")
                total += service.price
        
        print(f"\n💵 Итого к оплате: {total} руб.")
        print("\n1. ➕ Добавить услугу")
        print("2. ❌ Удалить услугу")
        print("0. ↩️ Назад к заказу")
        
        choice = input("👉 Выберите действие: ")

        if choice == "1":
            print("\n🔧 Доступные услуги:")
            services = get_all_services()
            for s in services:
                print(f"  🆔 {s.id}. {s.title} - {s.price} руб.")
            
            try:
                service_id = int(input("\nВведите ID услуги: "))
                service = get_service_by_id(service_id)
                if not service:
                    print("❌ Услуга не найдена!")
                    continue
                
                OrderItem(
                    order_id=order_id,
                    service_id=service_id
                ).save()
                
                order.total_amount = sum(s.price for s in [get_service_by_id(i.service_id) for i in get_items_by_order_id(order_id)])
                order.save()
                
                print(f"✅ Услуга '{service.title}' добавлена в заказ!")
                
            except ValueError:
                print("❌ Неверный формат ID!")

        elif choice == "2":
            if not items:
                print("ℹ️ Нет услуг для удаления")
                continue
                
            item_id = input("Введите ID позиции для удаления: ")
            try:
                OrderItem(id=int(item_id)).delete()
                
                remaining_items = get_items_by_order_id(order_id)
                if remaining_items:
                    order.total_amount = sum(s.price for s in [get_service_by_id(i.service_id) for i in remaining_items])
                else:
                    order.total_amount = 0
                order.save()
                
                print("🗑️ Услуга удалена из заказа!")
            except Exception as e:
                print(f"❌ Ошибка: {str(e)}")

        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод!")

def menu_orders():
    while True:
        print("\n🛒=== Управление заказами ===")
        print("👀 1. Показать все заказы")
        print("➕ 2. Создать новый заказ")
        print("❌ 3. Удалить заказ")
        print("🔧 4. Управление услугами в заказе")
        print("🔙 0. Назад в главное меню")
        
        choice = input("👉 Выберите действие: ")
        
        if choice == "1":
            orders = get_all_orders()
            print("\n📋 Список заказов:")
            for o in orders:
                client = get_client_by_id(o.client_id)
                print(f"🆔 {o.id}. 📅 {o.order_date} | 👤 {client.surname} {client.name} | 💰 {o.total_amount} руб.")
            if not orders:
                print("ℹ️ Нет созданных заказов")
                
        elif choice == "2":
            print("\n➕ Создание нового заказа")
            
            clients = get_all_clients()
            print("\n👥 Доступные клиенты:")
            for c in clients:
                print(f"  🆔 {c.id}. {c.surname} {c.name}")
            
            try:
                client_id = int(input("\nВведите ID клиента: "))
                if not any(c.id == client_id for c in clients):
                    print("❌ Клиент не найден!")
                    continue
                
                employees = get_all_employees()
                print("\n👨‍💼 Доступные сотрудники:")
                for e in employees:
                    print(f"  🆔 {e.id}. {e.surname} {e.name}")
                
                employee_id = int(input("\nВведите ID сотрудника: "))
                if not any(e.id == employee_id for e in employees):
                    print("❌ Сотрудник не найден!")
                    continue
                
                new_order = Order(
                    client_id=client_id,
                    employee_id=employee_id,
                    order_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    total_amount=0.0
                )
                new_order.save()
                print(f"✅ Заказ #{new_order.id} создан!")
                
                manage_order_items(new_order.id)
                
            except ValueError:
                print("❌ Неверный формат ID!")
                
        elif choice == "3":
            order_id = input("Введите ID заказа для удаления: ")
            try:
                Order(id=int(order_id)).delete()
                print("🗑️ Заказ удален!")
            except Exception as e:
                print(f"❌ Ошибка: {str(e)}")
                
        elif choice == "4":
            order_id = input("Введите ID заказа: ")
            try:
                if get_order_by_id(int(order_id)):
                    manage_order_items(int(order_id))
                else:
                    print("❌ Заказ не найден!")
            except ValueError:
                print("❌ Неверный формат ID!")
                
        elif choice == "0":
            break
            
        else:
            print("❌ Неверный ввод!")