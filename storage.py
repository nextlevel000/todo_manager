import json
import os
from models import Task

FILE_NAME = "tasks.json"

def save_tasks(tasks_list):
    data_to_save = []
    for task in tasks_list:
        data_to_save.append({
            "title": task.title,
            "is_done": task.is_done
        })
    
    with open(FILE_NAME, 'w', encoding='utf-8') as file:
        json.dump(data_to_save, file, indent=4, ensure_ascii=False)

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        loaded_dicts = json.load(file)
    
    tasks_list = []
    for dictionary in loaded_dicts:
        task = Task(dictionary["title"])
        task.is_done = dictionary["is_done"]
        tasks_list.append(task)
    
    return tasks_list