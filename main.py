tasks = []

menu = {
    1: "Add task",
    2: "View tasks",
    3: "Remove task",
    4: "Exit"
}


def todo_list(tasks):
    while True:
        print("\n--- To-Do List ---")

        for number, option in menu.items():
            print(f"{number}. {option}")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                task = input("Enter the task: ")
                tasks.append(task)
                print("Task added successfully.")

            elif choice == 2:
                if not tasks:
                    print("The task list is empty.")
                else:
                    print("\nYour Tasks:")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")

            elif choice == 3:
                if not tasks:
                    print("The task list is empty.")
                else:
                    print("\nYour Tasks:")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")

                    task_number = int(input("Enter the task number you want to delete: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f'Task "{removed_task}" removed successfully.')
                    else:
                        print("Invalid task number.")

            elif choice == 4:
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")


todo_list(tasks)