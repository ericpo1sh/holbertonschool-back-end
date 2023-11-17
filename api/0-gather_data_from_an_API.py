#!/usr/bin/python3
""" Gather Data Module """
import requests
from sys import argv


def gather_data_from_api(user_id):
    """ Gathering data from api """
    url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{url}/todos"
    employee_url = f"{url}/users/{user_id}"

    response = requests.get(employee_url)

    if response.status_code == 200:
        employee_data = response.json()
        name = employee_data.get("name")

        response = requests.get(todo_url, params={"userId": user_id})

        todo_data = response.json()
        fin_tasks = [task["title"] for task in todo_data if task["completed"]]
        completed_tasks = len(fin_tasks)
        total_tasks = len(todo_data)

        print("Employee {} is done with tasks({}/{}):"
              .format(name, completed_tasks, total_tasks))
        for title in fin_tasks:
            print(f"\t {title}")


if __name__ == "__main__":
    user_id = argv[1]
    gather_data_from_api(user_id)
