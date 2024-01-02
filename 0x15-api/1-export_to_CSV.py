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

    with open('{}.csv'.format(emplyId), 'w') as file:
        for t in tasks:
            file.write('"{}","{}","{}","{}"\n'
                       .format(emplyId, emplyName, t.get('completed'),
                               t.get('title')))
