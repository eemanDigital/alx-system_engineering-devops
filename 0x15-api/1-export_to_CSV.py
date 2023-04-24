#!/usr/bin/python3
"""Script to exports data of a given employee in CSV format."""

import csv
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    api_url = "https://jsonplaceholder.typicode.com/"
    user_res = requests.get(api_url + "users/{}".format(user_id)).json()
    username = user_res.get("username")
    todos_res = requests.get(api_url + "todos", params={
        "userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, x.get("completed"), x.get("title")]
         ) for x in todos_res]
