#!/usr/bin/python3
""" gathers data from an API """
from sys import argv
from requests import get
user = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
tasks = get(f'https://jsonplaceholder.typicode.com/todos')
user = user.json()
tasks = tasks.json()

e_id = argv[1]
e_name = u.get('name')
with open(f'{e_id}.csv', 'w') as file_name:
    csv_writer = csv.writer(file_name)
    for row in tasks:
        if row.get('userId') == e_id:
            temp = [e_id, e_name, row.get('completed'), row.get('title')]
