#!/usr/bin/python3
"""python scrpit that returns todo list from given API"""

import csv
import requests
from sys import argv


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
    """export to CSV"""
    csvname = ("{}.csv".format(argv[1]))
    with open(csvname, "w") as csvfile:
        fieldnames = ["USER_ID", "USERNAME",
                      "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(
            csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        for x in TASK_TITLE:
            writer.writerow(
                {"USER_ID": argv[1], "USERNAME": USERNAME,
                 "TASK_COMPLETED_STATUS": x[0],
                 "TASK_TITLE": x[1]})


if __name__ == "__main__":
    func()
