#!/usr/bin/python3
"""
    export data in csv format
"""

import requests
import sys
import csv

if __name__ == '__main__':
    user_id = sys.argv[1]
    count = 0
    params = {'id': user_id}
    todo_params = {'userId': user_id}
    user_info_url = 'https://jsonplaceholder.typicode.com/users'
    user_info = requests.get(user_info_url, params=params)
    employee = user_info.json()[0]
    employee_name = employee['name']
    todo_info_url = 'https://jsonplaceholder.typicode.com/todos'
    todo_info = requests.get(todo_info_url, params=todo_params)
    todos = todo_info.json()
    filename = '{}.csv'.format(user_id)
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        for row in todos:
            writer.writerow([user_id, employee_name, 
            row.get('completed'), row.get('title')])
