#!/usr/bin/python3
"""Exports todo information of all employees into JSON format."""
import json
import requests

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    users_res = requests.get(api_url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(api_url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users_res}, jsonfile)
