#!/usr/bin/python3
"""
gathers data of a user from an API and prints the tasks
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    user = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    tasks = get(f'https://jsonplaceholder.typicode.com/todos')
    user = user.json()
    tasks = tasks.json()

    e_id = argv[1]
    e_name = user.get('name')
    t_total = 0
    t_completed = []
    for row in tasks:
        if row.get('userId') == int(e_id):
            t_total += 1
            if row.get('completed'):
                t_completed.append(row.get('title'))
    t_done = len(t_completed)
    print(f'Employee {e_name} is done with tasks({t_done}/{t_total}):')
    for task in t_completed:
        print(f'\t {task}')
