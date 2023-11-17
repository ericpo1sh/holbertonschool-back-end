#!/usr/bin/python3
""" Gather Data Module """
import json
import sys
import urllib.request


def gather_data_from_api(user_id):
    """ Gather data from api """
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    user_data = urllib.request.urlopen(user_url).read()
    todo_data = urllib.request.urlopen(todo_url).read()
    user = json.l
