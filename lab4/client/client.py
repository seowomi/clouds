import requests

API_URL = "http://localhost:5000/api/todoitems"


def list_todos():
    response = requests.get(API_URL)
    todos = response.json()
    print("\n=== Список задач ===")
    for todo in todos:
        status = "✅" if todo["isComplete"] else "❌"
        print(f'{todo["id"]}. {todo["name"]} {status}')
    print()


def view_todo():
    todo_id = input("Введите ID задачи: ")
    response = requests.get(f"{API_URL}/{todo_id}")
    if response.status_code == 200:
        todo = response.json()
        print(f'\nID: {todo["id"]}\nИмя: {todo["name"]}\nЗавершена: {todo["isComplete"]}')
    else:
        print("❗ Задача не найдена.")


def add_todo():
    name = input("Введите название задачи: ")
    complete = input("Завершена? (y/n): ").strip().lower() == 'y'
    data = {
        "name": name,
        "isComplete": complete,
        "secret": "не скажу"  # это поле уйдёт, но сервер его примет (и скроет)
    }
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        print("✅ Задача добавлена.")
    else:
        print("❗ Ошибка добавления.")


def update_todo():
    todo_id = input("Введите ID задачи для обновления: ")
    name = input("Новое имя задачи: ")
    complete = input("Завершена? (y/n): ").strip().lower() == 'y'
    data = {
        "id": int(todo_id),
        "name": name,
        "isComplete": complete
    }
    response = requests.put(f"{API_URL}/{todo_id}", json=data)
    if response.status_code == 204:
        print("✅ Задача обновлена.")
    else:
        print("❗ Ошибка обновления.")


def delete_todo():
    todo_id = input("Введите ID задачи для удаления: ")
    response = requests.delete(f"{API_URL}/{todo_id}")
    if response.status_code == 204:
        print("🗑️ Задача удалена.")
    else:
        print("❗ Задача не найдена или уже удалена.")


def main():
    while True:
        print("\n📌 Меню:")
        print("1. Показать все задачи")
        print("2. Посмотреть задачу по ID")
        print("3. Добавить задачу")
        print("4. Обновить задачу")
        print("5. Удалить задачу")
        print("0. Выйти")

        choice = input("Выбор: ").strip()

        if choice == "1":
            list_todos()
        elif choice == "2":
            view_todo()
        elif choice == "3":
            add_todo()
        elif choice == "4":
            update_todo()
        elif choice == "5":
            delete_todo()
        elif choice == "0":
            print("👋 Пока!")
            break
        else:
            print("❗ Неверный ввод. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()
