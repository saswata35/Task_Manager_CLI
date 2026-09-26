import json
import datetime
import uuid

from src.config import DB_FILENAME, COMPLETE, PENDING
from .errors import TaskNotFound


def get_data():
    try:
        # Read all tasks from the JSON file
        with open(DB_FILENAME, "r", encoding="utf-8") as file:
            return json.load(file)

    # Return an empty list if the file is missing or contains invalid JSON
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data(data):
    # Save the updated task list in a readable JSON format
    with open(DB_FILENAME, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def find_task_index(data, task_id):
    # Find the task index while preserving its position in the list
    for index, task in enumerate(data):
        if task["id"] == task_id:
            return index

    return None


def add_task(name):
    data = get_data()
    current_time = datetime.datetime.now().isoformat(timespec="seconds")

    task = {
        # Convert UUID to string because JSON cannot store UUID objects
        "id": str(uuid.uuid4()),
        "name": name,
        "status": PENDING,
        "created_at": current_time,
        "updated_at": current_time
    }

    data.append(task)
    save_data(data)

    return task


def update_task(id, name, status):
    data = get_data()
    index = find_task_index(data, id)

    if index is None:
        raise TaskNotFound(f"Task: '{id}' not found")

    # Accept only the two statuses defined in config.py
    if status not in (PENDING, COMPLETE):
        raise ValueError(
            f"Status must be '{PENDING}' or '{COMPLETE}'"
        )

    # Update the same dictionary without changing its list position
    data[index]["name"] = name
    data[index]["status"] = status
    data[index]["updated_at"] = (
        datetime.datetime.now().isoformat(timespec="seconds")
    )

    save_data(data)

    return data[index]


def delete_task(id):
    data = get_data()
    index = find_task_index(data, id)

    if index is None:
        raise TaskNotFound(f"Task: '{id}' not found")

    # Remove and return the selected task
    removed_task = data.pop(index)
    save_data(data)

    return removed_task


def read_task(id):
    data = get_data()
    index = find_task_index(data, id)

    if index is None:
        raise TaskNotFound(f"Task: '{id}' not found")

    return data[index]