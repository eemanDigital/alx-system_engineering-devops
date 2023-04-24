#!/usr/bin/python3

"""
Script that uses an API to return information about
employee's TODO list progress.

"""

import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    user_res = requests.get(api_url + "users/{}".format(sys.argv[1])).json()

    todos_res = requests.get(api_url + "todos", params={
        "userId": sys.argv[1]}).json()

    completed_task = [x.get("title") for x in todos_res if x.get(
        "completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        user_res.get("name"), len(completed_task), len(todos_res)))

    [print("\t {}".format(com)) for com in completed_task]
