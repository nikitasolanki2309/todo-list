menu = {
    1: "Add task",
    2: "View tasks",
    3: "Remove task",
    4: "Mark task as completed",
    5: "Mark task as pending",
    6: "Search tasks",
    7: "Filter tasks",
    8: "Exit"
}


def load_tasks():
    tasks = []

    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                line = line.strip()

                if not line:
                    continue

                parts = line.rsplit("|", 2)

                if len(parts) == 3:
                    task_name, status, priority = parts
                elif len(parts) == 2:
                    task_name, status = parts
                    priority = "Medium"
                else:
                    task_name = parts[0]
                    status = "pending"
                    priority = "Medium"

                tasks.append({
                    "task": task_name,
                    "completed": status == "completed",
                    "priority": priority
                })

    except FileNotFoundError:
        pass

    return tasks


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            status = "completed" if task["completed"] else "pending"

            file.write(
                f'{task["task"]}|{status}|{task["priority"]}\n'
            )


def view_tasks(tasks):
    if not tasks:
        print("The task list is empty.")
        return

    print("\nYour Tasks:")

    for number, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"

        print(
            f'{number}. {task["task"]} '
            f'[{status}] [{task["priority"]}]'
        )


def add_task(tasks):
    task_name = input("Enter the task: ").strip()

    if not task_name:
        print("Task cannot be empty.")
        return

    print("\nSelect Priority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    try:
        choice = int(input("Enter priority choice: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    priorities = {
        1: "High",
        2: "Medium",
        3: "Low"
    }

    if choice not in priorities:
        print("Invalid priority choice.")
        return

    tasks.append({
        "task": task_name,
        "completed": False,
        "priority": priorities[choice]
    })

    save_tasks(tasks)
    print("Task added successfully.")


def remove_task(tasks):
    if not tasks:
        print("The task list is empty.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter the task number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if 1 <= number <= len(tasks):
        removed_task = tasks.pop(number - 1)
        save_tasks(tasks)

        print(f'Task "{removed_task["task"]}" removed successfully.')
    else:
        print("Invalid task number.")


def change_status(tasks, completed):
    if not tasks:
        print("The task list is empty.")
        return

    view_tasks(tasks)

    try:
        number = int(input("Enter the task number: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if not 1 <= number <= len(tasks):
        print("Invalid task number.")
        return

    task = tasks[number - 1]

    if task["completed"] == completed:
        if completed:
            print("This task is already completed.")
        else:
            print("This task is already pending.")
        return

    task["completed"] = completed
    save_tasks(tasks)

    if completed:
        print("Task marked as completed.")
    else:
        print("Task marked as pending.")


def search_tasks(tasks):
    if not tasks:
        print("The task list is empty.")
        return

    search_name = input("Enter task name to search: ").strip().lower()

    if not search_name:
        print("Search name cannot be empty.")
        return

    found_tasks = []

    for task in tasks:
        if search_name in task["task"].lower():
            found_tasks.append(task)

    if found_tasks:
        print("\nSearch Results:")
        view_tasks(found_tasks)
    else:
        print("No matching tasks found.")


def filter_tasks(tasks):
    filter_menu = {
        1: "Show pending tasks",
        2: "Show completed tasks",
        3: "Show high-priority tasks",
        4: "Show medium-priority tasks",
        5: "Show low-priority tasks",
        6: "Back to main menu"
    }

    while True:
        print("\n--- Filter Tasks ---")

        for number, option in filter_menu.items():
            print(f"{number}. {option}")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 6:
            break

        elif choice == 1:
            filtered = [
                task for task in tasks
                if not task["completed"]
            ]

        elif choice == 2:
            filtered = [
                task for task in tasks
                if task["completed"]
            ]

        elif choice == 3:
            filtered = [
                task for task in tasks
                if task["priority"] == "High"
            ]

        elif choice == 4:
            filtered = [
                task for task in tasks
                if task["priority"] == "Medium"
            ]

        elif choice == 5:
            filtered = [
                task for task in tasks
                if task["priority"] == "Low"
            ]

        else:
            print("Invalid choice.")
            continue

        view_tasks(filtered)


def todo_list(tasks):
    while True:
        print("\n--- To-Do List ---")

        for number, option in menu.items():
            print(f"{number}. {option}")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            add_task(tasks)

        elif choice == 2:
            view_tasks(tasks)

        elif choice == 3:
            remove_task(tasks)

        elif choice == 4:
            change_status(tasks, True)

        elif choice == 5:
            change_status(tasks, False)

        elif choice == 6:
            search_tasks(tasks)

        elif choice == 7:
            filter_tasks(tasks)

        elif choice == 8:
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


tasks = load_tasks()
todo_list(tasks)