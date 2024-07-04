from datetime import datetime
from colours import *

class Task:
    def __init__(self, description, due_date=None, priority=1):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = "Incomplete"

    def mark_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"{self.description} (Due: {self.due_date}, Priority: {self.priority}, Status: {self.status})"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def mark_task_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.mark_complete()
            print(f"Task '{task.description}' marked as complete.")
        else:
            print("Invalid task index.")

    def remove_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Complete"]
        print("Completed tasks removed.")

    def update_task(self, task_index, new_description, new_due_date, new_priority):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = new_description
            task.due_date = new_due_date
            task.priority = new_priority
            print(f"Task '{task.description}' updated.")
        else:
            print("Invalid task index.")

    def search_tasks(self, keyword):
        matching_tasks = [task for task in self.tasks if keyword.lower() in task.description.lower()]
        if matching_tasks:
            print(f"\n{BOLD}Matching tasks for '{keyword}':")
            for index, task in enumerate(matching_tasks, start=1):
                print(f"{index}. {task}")
        else:
            print(f"\n{BOLD}No matching tasks found for '{keyword}'.")

    def sort_tasks(self, criteria='due_date'):
        if criteria == 'due_date':
            self.tasks.sort(key=lambda task: task.due_date if task.due_date else datetime.max)
        elif criteria == 'priority':
            self.tasks.sort(key=lambda task: task.priority)
        elif criteria == 'status':
            self.tasks.sort(key=lambda task: task.status)
        else:
            print("Invalid sorting criteria.")

    def save_to_file(self, filename='tasks.txt'):
        try:
            with open(filename, 'w') as file:
                for task in self.tasks:
                    file.write(f"{task.description},{task.due_date},{task.priority},{task.status}\n")
            print(f"Tasks saved to {filename}.")
        except Exception as e:
            print(f"Error saving tasks to file: {e}")

    def load_from_file(self, filename='tasks.txt'):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    description, due_date_str, priority, status = data
                    due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
                    task = Task(description, due_date, int(priority))
                    task.status = status
                    self.tasks.append(task)
            print(f"Tasks loaded from {filename}.")
        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print(f"Error loading tasks from file: {e}")

def print_menu():
    print(f"""\n{CYAN}{BOLD}Choose an operation:{RESET}
\n{BOLD}1. Add Task
2. View Tasks
3. Mark Task as Complete
4. Remove Completed Tasks
5. Update Task
6. Search Tasks
7. Sort Tasks
8. Save to File
9. Load from File
10. Quit{RESET}""")

if __name__ == "__main__":
    my_todo_list = ToDoList()

    while True:
        try:
            print_menu()
            choice = input(f"\n{CYAN}{BOLD}Enter the number of your choice:{RESET} ")

            if choice == '1':
                description = input(f"\n{BOLD}Enter task description: ")
                due_date_str = input(f"{BOLD}Enter due date (YYYY-MM-DD), or press Enter for no due date: ")
                due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
                priority = int(input(f"{BOLD}Enter priority (1-5, 1 being the lowest): "))
                task = Task(description, due_date, priority)
                my_todo_list.add_task(task)

            elif choice == '2':
                my_todo_list.view_tasks()

            elif choice == '3':
                task_index = int(input(f"{BOLD}Enter the task number to mark as complete: "))
                my_todo_list.mark_task_complete(task_index)

            elif choice == '4':
                my_todo_list.remove_completed_tasks()

            elif choice == '5':
                task_index = int(input(f"{BOLD}Enter the task number to update: "))
                new_description = input(f"{BOLD}Enter new task description: ")
                new_due_date_str = input(f"{BOLD}Enter new due date (YYYY-MM-DD), or press Enter for no due date: ")
                new_due_date = datetime.strptime(new_due_date_str, "%Y-%m-%d") if new_due_date_str else None
                new_priority = int(input(f"{BOLD}Enter new priority (1-5, 1 being the lowest): "))
                my_todo_list.update_task(task_index, new_description, new_due_date, new_priority)

            elif choice == '6':
                search_keyword = input(f"{BOLD}Enter keyword to search tasks: ")
                my_todo_list.search_tasks(search_keyword)

            elif choice == '7':
                sort_criteria = input(f"{BOLD}Sort tasks by (due_date, priority, status): ")
                my_todo_list.sort_tasks(sort_criteria)

            elif choice == '8':
                filename = input(f"{BOLD}Enter the filename to save to (default: tasks.txt): ")
                my_todo_list.save_to_file(filename)

            elif choice == '9':
                filename = input(f"{BOLD}Enter the filename to load from (default: tasks.txt): ")
                my_todo_list.load_from_file(filename)

            elif choice == '10':
                break

            else:
                print(f"{BOLD}Invalid choice. Please enter a number between 1 and 10.{RESET}")

        except Exception as e:
            print(f"{BOLD}Error: {e}{RESET}")
