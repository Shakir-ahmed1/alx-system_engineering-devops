#!/usr/bin/python3
"""
gathers data from an API
"""
from json import dump
from requests import get

if __name__ == '__main__':
    user = get(f'https://jsonplaceholder.typicode.com/users')
    tasks = get(f'https://jsonplaceholder.typicode.com/todos')
    user = user.json()
    tasks = tasks.json()
    result = {}

    with open('todo_all_employees.json', 'w') as file_name:
        records = []
        for u in user:
            e_name = u.get('username')
            e_id = u.get('id')
            result = {}
            for row in tasks:
                if row.get('userId') == int(e_id):
                    temp = {
                            "username": e_name,
                            "task": row.get('title'),
                            "completed": row.get('completed'),
                            }
                    records.append(temp)
            result[str(e_id)] = records
        dump(result, file_name)
