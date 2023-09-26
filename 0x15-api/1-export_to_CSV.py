#!/usr/bin/python3
"""
gathers data from an API and stores the data of a user in a csv file
"""

from sys import argv
import csv
from requests import get

if __name__ == '__main__':
    user = get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    tasks = get(f'https://jsonplaceholder.typicode.com/todos')
    user = user.json()
    tasks = tasks.json()

    e_id = argv[1]
    e_name = user.get('name')
    with open(f'{e_id}.csv', 'w') as file_name:
        csv_writer = csv.writer(file_name, delimiter=",", quotechar='"',
                                quoting=csv.QUOTE_ALL)
        for row in tasks:
            if row.get('userId') == int(e_id):
                temp = [f'{e_id}',
                        f'{e_name}',
                        f'{row.get("completed")}',
                        f'{row.get("title")}']
                csv_writer.writerow(temp)
