from typing import List

from Task import Task as Task
from Status import Status as Status

taskList = []
taskFile = "tasks.txt"


def display_all_tasks():
    read_file = open(taskFile, "r")
    for line in read_file:
        convert_line_to_task(line)
    read_file.close()
    print(taskList)


def get_status_from_text(text: str) -> Status:
    return Status.from_string(text)


def convert_line_to_task(line: str) -> Task:
    task_and_status = line.split(":")
    task = Task(task_and_status[0].strip(), get_status_from_text(task_and_status[1].strip()))

    # print(f' converted line: \n {line} \n to task: \n {task} \n')
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
    try:
        if get_task_by_name(task.description):
            raise ValueError(f' "{task.description}" task matching that description already exists')
    except ValueError:
        pass

    taskList.append(task)
    print(f' Added task: \n {task} \n')
    write_tasks_to_file()


def get_task_by_name(description: str) -> Task:
    for task in taskList:
        if task.description.casefold() == description.casefold():
            return task
    raise ValueError(f"'{description}' task not found")


def _init_task_list() -> List[Task]:
    seen_tasks = set()
    with open(taskFile, "r") as file:
        line = file.readline()
        while line:
            task = convert_line_to_task(line)
            if task.description not in seen_tasks:
                taskList.append(task)
                seen_tasks.add(task.description)
            line = file.readline()

    return taskList


def write_tasks_to_file() -> None:
    with open(taskFile, "w") as file:
        for task in taskList:
            file.write(f"{task.description} : {task.status.value}\n")


_init_task_list()
print("Initial Tasks:")
display_all_tasks()

add_task_to_list(
    Task("Something to do"))

print("Updated Tasks:")
display_all_tasks()
