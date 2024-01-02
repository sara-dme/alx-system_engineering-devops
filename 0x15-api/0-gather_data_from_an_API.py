#!/usr/bin/python3
"""  script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    emplyId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    usr = url + "/" + emplyId

    res_user = requests.get(usr)
    emplyName = res_user.json().get('name')

    todo = usr + "/todos"
    res = requests.get(todo)
    tasks = res.json()
    done = 0
    done_tasks = []

    for t in tasks:
        if t.get('completed'):
            done_tasks.append(t)
            done += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(emplyName, done, len(tasks)))

    for t in done_tasks:
        print("\t {}".format(t.get('title')))
