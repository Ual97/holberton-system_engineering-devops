#!/usr/bin/python3
"""python scrpit that returns todo list from given API"""

import requests
from sys import argv


def func():
    """function to manage info from API's"""
    user = requests.get("https://jsonplaceholder.typicode.com/users")
    for i in user.json():
        if i.get('id') == int(argv[1]):
            EMPLOYEE_NAME = (i.get('name'))
            break
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_TASKS = 0
    TASK_TITLE = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    for j in todos.json():
        if j.get('userId') == int(argv[1]):
            if j.get('completed') is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(j.get('title'))
                TOTAL_TASKS += 1
            else:
                TOTAL_TASKS += 1

    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUMBER_OF_DONE_TASKS,
                                                          TOTAL_TASKS))
    for h in TASK_TITLE:
        print("\t {}".format(h))


if __name__ == "__main__":
    func()
