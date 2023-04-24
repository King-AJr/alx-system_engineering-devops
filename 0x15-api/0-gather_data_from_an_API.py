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
    employee_name = employee['name']

    todo_info_url = 'https://jsonplaceholder.typicode.com/todos'
    todo_info = requests.get(todo_info_url, params=todo_params)
    todos = todo_info.json()

    for i in todos:
        if i['completed'] == True:
            count += 1

    print(f"Employee {employee_name} is done with tasks({count}/{len(todos)}):")
    for i in todos:
        if i['completed'] == True:
            print(f"\t{i['title']}")

