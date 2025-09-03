tasks = []

def show_menu():
    print("\nTo-Do List:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if (choice == '1'):
        task = input("\nEnter task: ")
        tasks.append(task)
        print("Task added!")

    elif (choice == '2'):
        if (not tasks):
            print("No tasks found.")
        else:
            print("Your Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif (choice == '3'):
        try:
            task_num = int(input("Enter task number to delete: "))
            if (1 <= task_num <= len(tasks)):
                deleted = tasks.pop(task_num - 1)
                print(f"Deleted: {deleted}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

    elif (choice == '4'):
        print("Exiting To-Do List. Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
