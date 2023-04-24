#!/usr/bin/python3
""" take an employee id and fetch
    information about his/her TODO list progress.
    after which export info in json format"""
import json
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    count = 0
    params = {'id': user_id}
    todo_params = {'userId': user_id}
    user_info_url = 'https://jsonplaceholder.typicode.com/users'
    user_info = requests.get(user_info_url, params=params)
    employee = user_info.json()[0]
    emp_name = employee['name']

    todo_info_url = 'https://jsonplaceholder.typicode.com/todos'
    todo_info = requests.get(todo_info_url, params=todo_params)
    todos = todo_info.json()
    filename = "{}.json".format(user_id)
    with open(filename, 'w') as file:
        json.dump(todos, file)
