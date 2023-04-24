#!/usr/bin/python3

"""
Script that uses an API to return information about
employee's TODO list progress.

"""

import requests
import sys


if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"

    get_user = requests.get(api_url + "users/{}".format(sys.argv[1])).json()

    todos = requests.get(api_url + "todos", params={
        "userId": sys.argv[1]}).json()

    completed = [tt.get("title") for tt in todos if tt.get(
        "completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        get_user.get("name"), len(completed), len(todos)))

    [print("\t {}".format(com)) for com in completed]
