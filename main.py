from database.db_manager import initialize_db
from ui.menu import show_main_menu
from ui.menu_services import menu_services
from ui.menu_employees import menu_employees
from ui.menu_clients import menu_clients
from ui.menu_orders import menu_orders
from ui.menu_categories import menu_categories

def main():
    initialize_db()
    
    while True:
        choice = show_main_menu()
        
        if choice == "1":
            menu_categories()
        elif choice == "2":
            menu_services()
        elif choice == "3":
            menu_employees()
        elif choice == "4":
            menu_clients()
        elif choice == "5":
            menu_orders()
        elif choice == "0":
            print("\n👋 До свидания!")
            break
        else:
            print("❌ Неверный выбор!")

if __name__ == "__main__":
    main()