#!/usr/bin/python3
""" Export To CSV Module """
import json
import requests
from sys import argv


def export_to_JSON(user_id):
    """ Gathering data from api """
    url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{url}/users/{user_id}/todos"
    employee_url = f"{url}/users/{user_id}"
    users_response = requests.get(employee_url)
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()
    employee_data = users_response.json()
    name = employee_data.get("username")
    tasks = {task["title"]: task['completed'] for task in todo_data}
    new_dict = {user_id: list({
        'task': task,
        'completed': task_status,
        'username': name
    }
        for task, task_status in tasks.items()
    )}

    with open(f"{user_id}.json", "w") as newfile:
        json.dump(new_dict, newfile)


if __name__ == "__main__":
    user_id = int(argv[1])
    export_to_JSON(user_id)
