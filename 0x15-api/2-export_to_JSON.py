#!/usr/bin/python3
# Task 1
"""Python script to export data in the CSV format"""
if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys

    class mydict(dict):
        def __str__(self):
            return json.dumps(self)

    user = sys.argv[1]
    res = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format
                       (user)).json()
    res2 = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
                        .format(user)).json()
    list_dir = []
    for k in res2:
        if k['userId'] == int(user):
            to_list = {"task": k['title'],
                       "completed": k['completed'],
                       "username": res['username']}
            list_dir.append(to_list)
    list_out = []
    for v in list_dir:
        out = mydict(v)
        list_out.append(out)
    final = {'{}'.format(user): list_out}
    with open('{}.json'.format(user), 'w') as f:
        json.dump(final, f)
