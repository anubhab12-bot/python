import os
import json
from datetime import datetime

class ToDoList:
    def __init__(self, filename='todo.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=2)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task['description']} (Created: {task['created']})")

    def add_task(self, description):
        new_task = {
            'description': description,
            'created': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        self.tasks.append(new_task)
        self.save_tasks()
        print("Task added successfully.")

    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Task removed: {removed_task['description']}")
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\n1. Display Tasks\n2. Add Task\n3. Remove Task\n4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            todo_list.display_tasks()
        elif choice == '2':
            description = input("Enter task description: ")
            todo_list.add_task(description)
        elif choice == '3':
            todo_list.display_tasks()
            index = int(input("Enter the task index to remove: "))
            todo_list.remove_task(index)
        elif choice == '4':
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
