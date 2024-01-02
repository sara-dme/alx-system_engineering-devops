#!/usr/bin/python3
"""  script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys
import json

if __name__ == "__main__":
    emplyId = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/users"
    usr = url + "/" + emplyId

    res_user = requests.get(usr)
    name = res_user.json().get('username')

    todo = usr + "/todos"
    res = requests.get(todo)
    tasks = res.json()

    dictionary = {emplyId: []}
    for t in tasks:
        dictionary[emplyId].append({
            "task": t.get('title'),
            "completed": t.get('completed'),
            "username": name})
    with open('{}.json'.format(emplyId), 'w') as filename:
        json.dump(dictionary, filename)
