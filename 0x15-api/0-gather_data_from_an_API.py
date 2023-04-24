#!/usr/bin/python3
""" takes employee's id and returns
    information about his/her TODO list progress.
"""

import urllib.request as r
import urllib.parse as parse
import sys
import json


user_id = sys.argv[1]
count = 0
params = parse.urlencode({'id' : user_id})
todo_param = parse.urlencode({'userId': user_id})
user_info_url = 'https://jsonplaceholder.typicode.com/users'
user_info = f"{user_info_url}?{params}"
with r.urlopen(user_info) as response:
    employee = json.loads(response.read())
employee_name = employee[0]['name']



todo_info_url = 'https://jsonplaceholder.typicode.com/todos'
todo_info = f"{todo_info_url}?{todo_param}"
with r.urlopen(todo_info) as todo:
    todos = json.loads(todo.read())

for i in todos:
    if i['completed'] == True:
        count += 1


print(f"Employee {employee_name} is done with tasks({count}/{len(todos)}):")
for i in todos:
    if i['completed'] == True:
        print(f"\t{i['title']}")
