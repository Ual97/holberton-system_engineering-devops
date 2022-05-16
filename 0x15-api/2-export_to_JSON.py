#!/usr/bin/python3
"""python scrpit that returns todo list from given API"""

from sys import argv
import json
import requests


def func():
    """function to manage info from API's"""
    user = requests.get("https://jsonplaceholder.typicode.com/users")
    for i in user.json():
        if i.get('id') == int(argv[1]):
            USERNAME = (i.get('username'))
            break
    TASK_TITLE = []
    todos = requests.get("https://jsonplaceholder.typicode.com/todos")
    for j in todos.json():
        if j.get('userId') == int(argv[1]):
            TASK_TITLE.append((j.get('completed'), j.get('title')))
    """export to json"""
    t = []
    for x in TASK_TITLE:
        t.append({"task": x[1], "completed": x[0], "username": USERNAME})
    data = {str(argv[1]): t}
    filename = "{}.json".format(argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)


if __name__ == "__main__":
    func()
