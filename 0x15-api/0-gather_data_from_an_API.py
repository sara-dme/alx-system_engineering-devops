#!/usr/bin/python3
"""  script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

if __name__ == "__main__":
    emplyId = sys.argv[1]
    uurl = "https://jsonplaceholder.typicode.com/users"
    url = uurl + "/" + emplyId

    response = request.get(url)
    emplyName = reponse.json().get('name')

    todo = url + "/todo"
    response = request.get(todo)
    tasks = response.json()
    done = 0
    done_tasks = []

    for t in tasks:
        if t.get('completed'):
            done_tasks.append(t)
            done += 1

    print("Employee {} is done with tasks ({}/{}):"
          .format(emplyName, done, len(tasks)))

    for t in done_tasks:
        print("\t {}".format(t.get('title')))
