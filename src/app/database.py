import json
import datetime
import uuid
from src.config import DB_FILENAME, COMPLETE, PENDING
from .errors import TaskNotFound

def get_data():
    # TODO: Research for a better approach.
    with open(DB_FILENAME, "r",encoding = "utf-8") as f:
        # JSON -> DATA -> LOAD
        data = dict(json.load(f))

    return data

# Research for a better method to update a dict in the list without losing the actual index and without using unknown iterations of loop O(n)
# O(1)

def save_data(data):
    with open(DB_FILENAME, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def add_task(name):
    # TODO: Research for a better approach.
    
    # with open(DB_FILENAME, "r+", encoding = "utf-8") as f:
        
    # data = list(json.load(f))
   
    data = get_data()
    now = datetime.datetime.now().isoformat()
         
    task ={
        "name" : name,
        "status" : PENDING,
        "created_at": now,
        "updated_at" : now,
    }

    # data[str(uuid.uuid4())] = task

    data[f"{uuid.uuid4()}"] = task

    save_data(data)

    # values = list(data.values())
    
    # values.append(task)
    
    # DUMP -> DATA -> JSON 
    
    # json.dump(data, f)

    # save_data(values)
    
    return task

# Research for a better method to update a dict in the list without losing the actual index and without using unknown iterations of loop O(n)
# O(1)

def update_task(id, name, status):

    # TODO: Research for a better approach.
    # with open(DB_FILENAME, "r+", encoding= "utf-8") as f:
    #     data = list(json.load(f))

    #     find_item = lambda task : task["id"] == id

    #     try:
    #         task = list(filter(find_item, data)) [0]

    #     except IndexError:
    #         print(f"[ ERROR ]: {id}  not found in database.")

    #     else:
    #         task ["name"] = name
    #         task["status"] = status
    #         task["updated_at"] = datetime.datetime.now()

    #     for idx, item in enumerate(data):
    #         if item["id"] == id:
    #             data.pop(idx)
    #             data.insert(idx, task)

    # Research for a better method to update a dict in the list without losing the actual index and without using unknown iterations of loop O(n)
    # O(1)

    data = get_data()

    # [(key,value), ()]
    # for idx, value in data.items():
    #     if value["id"] == id:
    #         value["name"] = name
    #         value["status"] = status
    #         value["updated_at"] = datetime.datetime.now()

    task = data.get(id)

    if task:
        task["name"] = name
        task["status"] = status
        task["updated_at"] = datetime.datetime.now().isoformat()

        data[id] = task
        save_data(data)
        return task

    else:
        raise TaskNotFound(f"Task with id: '{id}' not found")

    
def delete_task(id):
    # TODO: Research for a better approach.
    # with open(DB_FILENAME, "r+", encoding= "utf-8") as f:
    #         data = list(json.load(f))
    
    #         find_item = lambda task : task["id"] == id

    #         # try:
    #         #     task = list(filter(find_item, data)) [0]
            
    #         # except IndexError:
    #         #     print(f"[ ERROR ]: {id}  not found in database.")
            
    #         # else: 
    #         for idx, item in enumerate(data):
    #             if item["id"] == id:
    #                 removed_task = data.pop(idx)

    #                 return removed_task
    #         # Research for a better method to update a dict in the list without losing the actual index and without using unknown iterations of loop O(n)
    #         # O(1)
    #             else:
    #                 raise TaskNotFound(f"Task: '{id}' not found")

    data = get_data()
    try:
        task = data.pop(id)
    except KeyError:
        raise TaskNotFound(f"Task with id: '{id}' not found")
    save_data(data)
    return task

def display_task(task_id, task):
    print(f"\nID         : {task_id}")
    print(f"Name       : {task['name']}")
    print(f"Status     : {task['status']}")
    print(f"Created At : {task['created_at']}")
    print(f"Updated At : {task['updated_at']}")

def read_task(id):
    # # TODO: Research for a better approach.
    # with open(DB_FILENAME, "r+", encoding= "utf-8") as f:
    #     data = list(json.load(f))

    #     find_item = lambda task : task["id"] == id

    #     try:
    #        task = list(filter(find_item, data)) [0]
         
    #     except IndexError:
    #        print(f"[ ERROR ]: {id}  not found in database.")
         
    # # Research for a better method to update a dict in the list without losing the actual index and without using unknown iterations of loop O(n)
    # # O(1)
    
    data = get_data()

    try:
        return data[id]
    except KeyError:
        raise TaskNotFound(f"Task with id: '{id}' not found")
