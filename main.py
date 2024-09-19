from typing import List
import os
from Task import Task
from Status import Status

# Constants
TASK_FILE = "tasks.txt"

# Task List
tasks: List[Task] = []


def display_all_tasks() -> None:
    """Display all tasks in the list."""
    print(tasks)


def get_status_from_text(text: str) -> Status:
    """Convert text to Status enum."""
    return Status.from_string(text)


def convert_line_to_task(line: str) -> Task:
    task_and_status = line.split(":")
    if len(task_and_status) != 2:
        raise ValueError(f' : is only allowed once in the line, between the description and the status')
    task = Task(task_and_status[0].strip(), get_status_from_text(task_and_status[1].strip()))
    return task


def initialize_task_list() -> None:
    """Initialize the task list by loading tasks from a file."""
    global tasks
    tasks.clear()
    unique_tasks = set()
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task = convert_line_to_task(line)
                if task.description not in unique_tasks:
                    tasks.append(task)
                    unique_tasks.add(task.description)


def get_task_by_name(description: str) -> Task:
    """Retrieve a task by its description."""
    for task in tasks:
        if task.description.casefold() == description.casefold():
            return task
    return None


def update_task_in_list(task: Task) -> None:
    """Update an existing task in the list."""
    task_index = tasks.index(get_task_by_name(task.description))
    tasks[task_index] = Task(task.description, task.status)
    write_tasks_to_file()


def add_task_to_list(task: Task) -> None:
    """Add a new task to the list."""
    if get_task_by_name(task.description) is not None:
        raise ValueError(f'Task "{task.description}" already exists')
    if ":" in task.description:
        raise ValueError(f'Task "{task.description}" contains invalid character: ":"')
    tasks.append(task)
    log_task_action('Added', task)
    write_tasks_to_file()


def write_tasks_to_file() -> None:
    """Write the current list of tasks to the file."""
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task.description} : {task.status.value}\n")


def log_task_action(action: str, task: Task) -> None:
    """Log task actions like adding or updating."""
    print(f'{action} task: \n {task} \n')


def main():
    """Main function to initialize and display tasks."""
    initialize_task_list()
    print("Initial Tasks:")
    display_all_tasks()

    add_task_to_list(Task("Something to do"))

    print("Updating Task:")
    update_task_in_list(Task("Something to do", Status.COMPLETED))
    display_all_tasks()

    print('Adding invalid task due to multiple : :')
    add_task_to_list(Task("read the book:  python for dummies"))


if __name__ == "__main__":
    main()
