from datetime import datetime

from loader import (
    load_tasks,
    save_tasks,
    load_done_tasks,
    save_done_tasks,
    load_in_progress,
    save_in_progress,
)

tasks = load_tasks()

 
class Task():
    def __init__(self,title,status = "todo",created_at=None):
        self.title = title
        self.status = status
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "created_at": self.created_at
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
    
    def mark_in_progress(self,index):
        self.tasks = load_tasks()
        task = self.tasks.pop(index-1)
        task["status"] = "in_progress"
        in_progress_task = load_in_progress()
        in_progress_task.append(task)
        save_tasks(self.tasks)
        save_in_progress(in_progress_task)


    def mark_done(self,index):
        self.tasks = load_tasks()
        task = self.tasks.pop(index-1)
        task["status"] = "done"
        done_tasks = load_done_tasks()
        done_tasks.append(task)
        save_tasks(self.tasks)
        save_done_tasks(done_tasks)
        
    
    def _list_tasks(self,tasks):
        if not tasks:
            print("No tasks found")
            return

        status_map ={
                "todo": " ",
                "in_progress": "~",
                "done": "✓"
            }
        
        for i, task in enumerate(tasks, start=1):
            status = status_map.get(task.get("status"), "?")
            created = task.get("created_at", "Unknown date")
            print(f"[{i}] [{status}] {task['title']} (created: {created})")
            
    def list_all_tasks(self):
        print(">>> list_all_tasks CALLED <<<")
        print("\nTODO:")
        self._list_tasks(load_tasks() or [])

        print("\nIN PROGRESS:")
        self._list_tasks(load_in_progress() or [])

        print("\nDONE:")
        self._list_tasks(load_done_tasks() or [])



    def list_tasks(self):
        self.tasks = load_tasks()
        self._list_tasks(self.tasks)
            

    def list_done_tasks(self):
        self.tasks = load_done_tasks()
        self._list_tasks(self.tasks)

    def list_in_progress_tasks(self):
        self.tasks = load_in_progress()
        self._list_tasks(self.tasks)