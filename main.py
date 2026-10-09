menu = {
    1: "Add task",
    2: "View tasks",
    3: "Remove task",
    4: "Mark task as completed",
    5: "Mark task as pending",
    6: "Exit"
}


def load_tasks():
    tasks = []

    try:
        with open("tasks.txt", "r") as file:
            for line in file.readlines():
                line = line.strip()

                if not line:
                    continue

                if "|" in line:
                    task_name, status = line.rsplit("|", 1)

                    tasks.append({
                        "task": task_name,
                        "completed": status == "completed"
                    })
                else:
                    tasks.append({
                        "task": line,
                        "completed": False
                    })

    except FileNotFoundError:
        pass

    return tasks


def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            status = "completed" if task["completed"] else "pending"

            file.write(f'{task["task"]}|{status}\n')


def view_tasks(tasks):
    if not tasks:
        print("The task list is empty.")
    else:
        print("\nYour Tasks:")

        for i, task in enumerate(tasks, start=1):
            status = "Completed" if task["completed"] else "Pending"

            print(f'{i}. {task["task"]} [{status}]')


def todo_list(tasks):
    while True:
        print("\n--- To-Do List ---")

        for number, option in menu.items():
            print(f"{number}. {option}")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                task_name = input("Enter the task: ").strip()

                if not task_name:
                    print("Task cannot be empty.")
                else:
                    tasks.append({
                        "task": task_name,
                        "completed": False
                    })

                    save_tasks(tasks)
                    print("Task added successfully.")

            elif choice == 2:
                view_tasks(tasks)

            elif choice == 3:
                if not tasks:
                    print("The task list is empty.")
                else:
                    view_tasks(tasks)

                    task_number = int(
                        input("Enter the task number you want to delete: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        save_tasks(tasks)

                        print(
                            f'Task "{removed_task["task"]}" '
                            "removed successfully."
                        )
                    else:
                        print("Invalid task number.")

            elif choice == 4:
                if not tasks:
                    print("The task list is empty.")
                else:
                    view_tasks(tasks)

                    task_number = int(
                        input("Enter the task number to mark as completed: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        task = tasks[task_number - 1]

                        if task["completed"]:
                            print("This task is already completed.")
                        else:
                            task["completed"] = True
                            save_tasks(tasks)
                            print("Task marked as completed.")
                    else:
                        print("Invalid task number.")

            elif choice == 5:
                if not tasks:
                    print("The task list is empty.")
                else:
                    view_tasks(tasks)

                    task_number = int(
                        input("Enter the task number to mark as pending: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        task = tasks[task_number - 1]

                        if not task["completed"]:
                            print("This task is already pending.")
                        else:
                            task["completed"] = False
                            save_tasks(tasks)
                            print("Task marked as pending.")
                    else:
                        print("Invalid task number.")

            elif choice == 6:
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")


tasks = load_tasks()
todo_list(tasks)