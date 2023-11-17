#!/usr/bin/python3
""" Export To CSV Module """
import csv
import requests
from sys import argv


def export_to_csv(user_id):
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

    with open(f'{user_id}.csv', 'w') as newfile:
        file_writer = csv.writer(newfile, quoting=csv.QUOTE_ALL)
        [
            file_writer.writerow([user_id, name, done_status, task])
            for task, done_status in tasks.items()
        ]


if __name__ == "__main__":
    user_id = int(argv[1])
    export_to_csv(user_id)
