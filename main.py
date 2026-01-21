from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:

        command = input("add/delete/complete/list/quit ").strip().lower()

        if command == "add":
            title = input("input title: ")
            manager.add_task(title)
        elif command == "delete":
            
            index = int(input("input number: "))
            manager.delete_task(index)
        elif command == "complete":
            index = int(input("input number: "))
            manager.complete_task(index)
        elif command == "list":
            if not manager.tasks:
                print("List is empty")
            manager.list_tasks()
        elif command == "quit":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()