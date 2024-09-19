from Task import Task as Task
from Status import Status as Status


def display_all_tasks():
    read_file = open("tasks.txt", "r")
    for line in read_file:
        convert_line_to_task(line)
    read_file.close()


def get_status_from_line(line: str) -> Status:
    return Status.from_string(line)


def convert_line_to_task(line: str) -> Task:
    task_and_status = line.split(":")
    task = Task(task_and_status[0].strip(), get_status_from_line(task_and_status[1].strip()))

    print(f' converted line: \n {line} \n to task: \n {task} \n')
    return task


display_all_tasks()
