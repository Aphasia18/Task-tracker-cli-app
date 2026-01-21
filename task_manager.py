import json
import os
TASKS_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks,file,indent=4)



class Task():
    def __init__(self,title,complete = False):
        self.title = title
        self.complete = complete
    
    def to_dict(self):
        return {
            "title": self.title,
            "complete": self.complete
        }
    

class TaskManager():
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self,title):
        self.tasks = load_tasks()
        task = Task(title)
        self.tasks.append(task.to_dict())

        save_tasks(self.tasks)

    def delete_task(self,index):
        self.tasks = load_tasks()
        self.tasks.pop(index - 1)
        save_tasks(self.tasks)
    
    def complete_task(self,index):
        self.tasks = load_tasks()
        self.tasks[index - 1]["complete"] = True
        save_tasks(self.tasks)
    
    def list_tasks(self):
        self.tasks = load_tasks()

        if not self.tasks:
            print("No tasks found")
            return
        
        for i, task in enumerate(self.tasks, start=1):
            status = "✓" if task["complete"] else " "
            print(f"[{i}] [{status}] {task['title']}")
