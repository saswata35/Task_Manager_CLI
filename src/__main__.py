import os

from src.app import database as db
from src.app import logger
from src.app.errors import TaskNotFound
from src.config import COMPLETE, DB_FILENAME, PENDING


if not os.path.exists(DB_FILENAME):
    with open(DB_FILENAME, "w", encoding="utf-8") as file:
        file.write("{}")


MENU = [
    "CREATE TASK",
    "UPDATE TASK",
    "DELETE TASK",
    "VIEW TASK",
    "VIEW ALL TASKS",
    "EXIT",
]



def main():
    print("-----TASK MANAGER CLI APPLICATION-----")
    for index, option in enumerate(MENU, start=1):
        print(f"> {index} - {option}")

    try:
        choice = int(input(">>> "))
    except ValueError:
        print("Please enter a number from 1 to 6.")
        return True

    match choice:
        case 1:
            name = input(">>> Enter Task Name: ").strip()
            if not name:
                print("Task name did not meet the requirements.")
                return True
            task = db.add_task(name)
            print(f"-> Task added: {task}")
            

        case 2:
            task_id = input(">>> Enter Task ID: ").strip()
            name = input(">>> Enter New Task Name: ").strip()
            status = input(">>> Enter Status (pending/complete): ").strip().lower()
            if not name:
                print("Task name did not meet the requirements.")
                return True
            if status not in (PENDING, COMPLETE):
                print("Status must be 'pending' or 'complete'.")
                return True
            try:
                task = db.update_task(task_id, name, status)
                print(f"-> Task updated: {task}")
            except TaskNotFound as error:
                print(f"[ERROR]: {error}")

        case 3:
            task_id = input(">>> Enter Task ID: ").strip()
            try:
                task = db.delete_task(task_id)
                print(f"-> Task deleted: {task}")
            except TaskNotFound as error:
                print(f"[ERROR]: {error}")

        case 4:
            task_id = input(">>> Enter Task ID: ").strip()
            try:
                db.display_task(task_id, db.read_task(task_id))
            except TaskNotFound as error:
                print(f"[ERROR]: {error}")

        case 5:
            data = db.get_data()
            if not data:
                print("No tasks found.")
            else:
                for task_id, task in data.items():
                    db.display_task(task_id, task)

        case 6:
            print("Task Manager closed.")
            return False

        case _:
            logger.warning("Unknown Choice")
            print("Please enter a number from 1 to 6.")

    return True


if __name__ == "__main__":
    try:
        while main():
            print()
    except (KeyboardInterrupt, EOFError):
        print("\nTask Manager closed.")
