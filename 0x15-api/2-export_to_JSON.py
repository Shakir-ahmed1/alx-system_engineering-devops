#!/usr/bin/python3
"""
gathers data from an API
"""
from sys import argv
from json import dump
from requests import get

if __name__ == '__main__':
    user = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    tasks = get(f'https://jsonplaceholder.typicode.com/todos')
    user = user.json()
    tasks = tasks.json()

    e_id = argv[1]
    e_name = user.get('username')
    with open(f'{e_id}.json', 'w') as file_name:
        records = []
        for row in tasks:
            if row.get('userId') == int(e_id):
                temp = {"task": row.get('title'),
                        "completed": row.get('completed'),
                        "username": e_name}
                records.append(temp)
        dump({str(e_id): records}, file_name)
