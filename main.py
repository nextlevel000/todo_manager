from models import Task          # Берем чертеж задачи
from storage import load_tasks, save_tasks  # Берем функции сохранения и загрузки

# 1. Загружаем задачи при старте 
tasks = load_tasks()
print("Добро пожаловать в Менеджер задач!")


# 2. Определяем функции-рецепты для меню 

def show_menu():
    """Показывает список доступных команд"""
    print("\n" + "="*30)
    print("1. Показать все задачи")
    print("2. Добавить задачу")
    print("3. Отметить задачу выполненной")
    print("4. Выйти")
    print("="*30)

def show_tasks():
    """Печатает все задачи с номерами"""
    if len(tasks) == 0:
        print("📭 У вас пока нет задач.")
        return
    
    print("\n--- ВАШИ ЗАДАЧИ ---")
    for i in range(len(tasks)):
        task = tasks[i]  # Достаем задачу по номеру
        status = "✅" if task.is_done else "❌"  # Если True - галочка, если False - крестик
        print(f"{i+1}. {status} {task.title}")

def add_task():
    """Спрашивает название и добавляет задачу"""
    title = input("Введите название задачи: ")
    if title == "":
        print("❌ Название не может быть пустым!")
        return
    
    new_task = Task(title)  # Создаем новый объект по чертежу
    tasks.append(new_task)  # Кладем в наш общий список
    save_tasks(tasks)       # СОХРАНЯЕМ в файл!
    print(f"✅ Задача '{title}' добавлена!")

def mark_done():
    """Отмечает задачу выполненной"""
    show_tasks()  # Сначала показываем список, чтобы пользователь видел номера
    if len(tasks) == 0:
        return
    
    try:
        number = int(input("Введите номер задачи, которую выполнили: "))
        # Проверяем, что номер существует (от 1 до количества задач)
        if 1 <= number <= len(tasks):
            tasks[number-1].is_done = True  # Меняем статус на True
            save_tasks(tasks)               # СОХРАНЯЕМ изменения!
            print(f"🎉 Задача выполнена!")
        else:
            print("❌ Нет задачи с таким номером.")
    except ValueError:
        print("❌ Ошибка! Введите именно число.")


# --- 3. Главный вечный цикл (программа работает, пока не скажут "Выйти") ---
while True:
    show_menu()
    choice = input("Выберите действие (1-4): ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        print("👋 До свидания! Данные сохранены.")
        break  # break вырывает нас из вечного цикла, программа закрывается
    else:
        print("⚠️ Неверный выбор, введите цифру от 1 до 4.")