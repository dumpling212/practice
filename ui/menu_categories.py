from models.category import Category, get_all_categories, get_category_by_id

def menu_categories():
    while True:
        print("\n🗂=== Управление категориями ===")
        print("👀 1. Показать все категории")
        print("➕ 2. Добавить категорию")
        print("❌ 3. Удалить категорию")
        print("✏️ 4. Изменить категорию")
        print("🔙 0. Назад в главное меню")
        
        choice = input("👉 Выберите действие: ")
        
        if choice == "1":
            categories = get_all_categories()
            print("\n📋 Список категорий:")
            for c in categories:
                print(f"🏷 {c.id}. {c.title}")
                
        elif choice == "2":
            title = input("\nНазвание категории: ")
            Category(title=title).save()
            print("✅ Категория добавлена!")
            
        elif choice == "3":
            cat_id = input("Введите ID категории для удаления: ")
            Category(id=int(cat_id)).delete()
            print("🗑️ Категория удалена!")
            
        elif choice == "4":
            cat_id = int(input("Введите ID категории для редактирования: "))
            cat = get_category_by_id(cat_id)
            cat.title = input(f"Новое название [{cat.title}]: ") or cat.title
            cat.save()
            print("✅ Категория обновлена!")
            
        elif choice == "0":
            break
        else:
            print("❌ Неверный ввод!")