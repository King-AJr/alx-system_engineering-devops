#!/usr/bin/python3
""" take an employee id and fetch
    information about his/her TODO list progress."""
import json
import requests

if __name__ == '__main__':
    user_info_url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(user_info_url).json()
    filename = "todo_all_employees.json"
    with open(filename, 'w') as file:
        json.dump({
            user.get("id"): [{
                "task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username")
            } for todo in requests.get("https://jsonplaceholder.typicode.com/todos",
                                    params={"userId": user.get("id")}).json()]
            for user in users}, file)
