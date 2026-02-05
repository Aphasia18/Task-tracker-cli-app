from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n--- Task Manager ---")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task as in progress")
        print("4. Mark task as done")
        print("5. Delete task")
        print("6. List done tasks")
        print("7. List in progress tasks")
        print("8. List all tasks")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            manager.list_tasks()

        elif choice == "2":
            title = input("Task title: ")
            manager.add_task(title)

        elif choice == "3":
            manager.list_tasks()
            index = int(input("Task number to mark in progress: "))
            manager.mark_in_progress(index)

        elif choice == "4":
            manager.list_tasks()
            index = int(input("Task number to mark done: "))
            manager.mark_done(index)

        elif choice == "5":
            manager.list_tasks()
            index = int(input("Task number to delete: "))
            manager.delete_task(index)

        elif choice == "6":
            manager.list_done_tasks()
        
        elif choice == "7":
            manager.list_in_progress_tasks()
        elif choice =="8":
            manager.list_all_tasks()
            
        elif choice == "9":
            print("Goodbye 👋")
            break

        else:
            print("Invalid option")

if __name__ == "__main__":
    main()