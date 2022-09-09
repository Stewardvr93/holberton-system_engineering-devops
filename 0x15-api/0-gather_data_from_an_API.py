#!/usr/bin/python3
# Task 0
"""Write a Python script that, using this REST API,
and return information about the progress of your TODO list.."""
if __name__ == "__main__":
    import json
    import sys
    from urllib.request import urlopen

    user = sys.argv[1]
    urlUser = 'https://jsonplaceholder.typicode.com/users/' + user
    r = urlopen(urlUser)
    dataUser = json.loads(r.read().decode(r.info().get_param('charset')))

    user = int(sys.argv[1])
    urlTodo = 'https://jsonplaceholder.typicode.com/todos/'
    r2 = urlopen(urlTodo)
    dataTodo = json.loads(r2.read().decode(r2.info().get_param('charset')))
    todo = 0
    falses = 0
    completed = []
    for x in dataTodo:
        if 'userId' in x:
            if x.get('userId') == user:
                todo += 1
                if x.get('completed') is False:
                    falses += 1
                else:
                    completed.append(x.get('title'))

    EMPLOYEE_COMPLETED = todo - falses
    EMPLOYEE_NAME = dataUser.get('name')
    print('Employee {} is done with tasks({}/{}):'.format(EMPLOYEE_NAME,
                                                          EMPLOYEE_COMPLETED,
                                                          todo))
    for comp in completed:
        print('\t '+comp)
