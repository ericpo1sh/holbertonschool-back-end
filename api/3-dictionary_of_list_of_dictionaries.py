#!/usr/bin/python3
""" Export To JSON Module """
import json
import requests


def dict_of_dicts():
    """ Gathering data from api """
    all_dict = {}
    for user_id in range(1, 11):
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
            'username': name,
            'task': task,
            'completed': task_status
        }
            for task, task_status in tasks.items()
        )}
        all_dict.update(new_dict)
    with open("todo_all_employees.json", "w") as newfile:
        json.dump(all_dict, newfile)


if __name__ == "__main__":
    dict_of_dicts()
