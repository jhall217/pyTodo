from typing import List
from Task import Task as Task
from Status import Status as Status
import os

taskList: List[Task] = []
taskFile = "tasks.txt"


def display_all_tasks():
    print(taskList)


def get_status_from_text(text: str) -> Status:
    return Status.from_string(text)


def convert_line_to_task(line: str) -> Task:
    task_and_status = line.split(":")
    task = Task(task_and_status[0].strip(), get_status_from_text(task_and_status[1].strip()))
    return task


def update_task_status(task: Task, new_status: Status) -> Task:
    task.status = new_status
    return task


def update_task_in_list(task: Task) -> None:
    task_index = taskList.index(get_task_by_name(task.description))
    task_to_update = taskList[task_index]
    task_to_update.description = task.description
    task_to_update.status = task.status
    taskList[task_index] = task_to_update
    write_tasks_to_file()


def add_task_to_list(task: Task) -> None:
    if get_task_by_name(task.description) is not None:
        raise ValueError(f'Task "{task.description}" already exists')
    taskList.append(task)
    print(f' Added task: \n {task} \n')
    write_tasks_to_file()


def get_task_by_name(description: str) -> Task:
    for task in taskList:
        if task.description.casefold() == description.casefold():
            return task
    return None


def _init_task_list():
    global taskList
    taskList.clear()  # Clear the task list to avoid duplicates
    seen_tasks = set()

    if os.path.exists(taskFile):
        with open(taskFile, "r") as file:
            for line in file:
                task = convert_line_to_task(line)
                if task.description not in seen_tasks:
                    taskList.append(task)
                    seen_tasks.add(task.description)


def write_tasks_to_file() -> None:
    with open(taskFile, "w") as file:
        for task in taskList:
            file.write(f"{task.description} : {task.status.value}\n")


# Initialize task list (load from file) and display initial tasks
_init_task_list()
print("Initial Tasks:")
display_all_tasks()

# Add a new task
add_task_to_list(Task("Something to do"))

print("Updating Task:")
update_task_in_list(Task("Something to do", Status.COMPLETED))
display_all_tasks()
