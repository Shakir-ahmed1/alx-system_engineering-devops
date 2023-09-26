#!/usr/bin/python3
"""
gathers data from an API
"""
from os import argv
from requests import get
from json import dump

user = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
tasks = get(f'https://jsonplaceholder.typicode.com/todos')
user = user.json()
tasks = tasks.json()

e_id = argv[1]
e_name = u.get('name')
with open(f'{e_id}.json', 'w') as file_name:
    records = []
    for row in tasks:
        if row.get('userId') == e_id:
            temp = {"task": row.get('title'),
                    "completed": row.get('completed'),
                    "username": e_name}
            records.append(temp)
    dump(file_name, {str(e_id): records})
