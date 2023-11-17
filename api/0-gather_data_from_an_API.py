#!/usr/bin/python3
""" Gathering data from an API """
import requests
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    user_id = argv[1]
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
