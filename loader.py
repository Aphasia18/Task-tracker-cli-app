import os
import json

TASKS_FILE = "tasks.json"
DONE_TASKS ="done.json"
IN_PROGRESS = "in_progress.json"

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    
    with open(TASKS_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks,file,indent=4)

def load_done_tasks():
    if not os.path.exists(DONE_TASKS):
        return []

    with open (DONE_TASKS,"r") as file:
        return json.load(file)
    
def save_done_tasks(done_tasks):
    with open(DONE_TASKS,"w") as file:
        json.dump(done_tasks,file,indent = 4)


def load_in_progress():
    if not os.path.exists(IN_PROGRESS):
        return []
    
    with open (IN_PROGRESS, "r") as file:
        return json.load(file)

def save_in_progress(in_progress):
    with open(IN_PROGRESS,"w") as file:
        json.dump(in_progress,file,indent=4)