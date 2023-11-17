#!/usr/bin/python3
""" Gather Data Module """
import requests
from sys import argv


def gather_data_from_api(user_id):
    """ Gathering data from api """
    url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{url}/todos"
    employee_url = f"{url}/users/{user_id}"
    users_response = requests.get(employee_url).json()
    employee_data = users_response.json()
    name = employee_data.get("name")
    todo_response = requests.get(todo_url, params={"userId": user_id}).json()
    todo_data = todo_response.json()
    fin_tasks = [task["title"] for task in todo_response if task["completed"]]
    completed_tasks = len(fin_tasks)
    total_tasks = len(todo_data)

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed_tasks, total_tasks))
    for title in fin_tasks:
        print(f"\t {title}")


if __name__ == "__main__":
    user_id = int(argv[1])
    gather_data_from_api(user_id)
