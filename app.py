import os

DATA_FILE = "/data/tasks.txt"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return [line.strip() for line in f.readlines()]

def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        f.write("\n".join(tasks))

def main():
    tasks = load_tasks()
    while True:
        print("\nВаши задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print("\nЧто вы хотите сделать?")
        print("1. Добавить задачу")
        print("2. Удалить задачу")
        print("3. Выйти")
        choice = input("Введите число: ")
        if choice == "1":
            task = input("Введите задачу: ")
            tasks.append(task)
            save_tasks(tasks)
        elif choice == "2":
            index = int(input("Введите номер задачи для удаления: ")) - 1
            if 0 <= index < len(tasks):
                tasks.pop(index)
                save_tasks(tasks)
        elif choice == "3":
            break
        else:
            print("Неверный выбор")

if __name__ == "__main__":
    main()
