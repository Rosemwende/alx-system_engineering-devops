#!/usr/bin/python3
"""Python script that, using this REST API,
for a given employee ID,
returns and exports information about his/her TODO list progress in JSON format.
"""

import json
import requests
from sys import argv

def get_employee_todos_progress(employee_id):
    """Fetches and returns the employee's todos progress"""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_datas = requests.get("{}users/{}".format(url, employee_id))
        user_data = user_datas.json()
        employee_name = user_data['name']
        username = user_data['username']

        """fetch the employee's todos list"""
        todos_list = requests.get("{}todos?userId={}".format(url, employee_id))
        json_todos_list = todos_list.json()

        """Prepare the data for JSON export"""
        tasks_list = []
        for task in json_todos_list:
            tasks_list.append({
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            })

        """Create the final dictionary to be exported"""
        user_tasks = {employee_id: tasks_list}

        """Write the JSON data to a file"""
        with open(f"{employee_id}.json", "w") as json_file:
            json.dump(user_tasks, json_file)

        """Display the result"""
        total_task = len(json_todos_list)
        task_done = len([task for task in json_todos_list if task['completed']])
        print(f"Employee {employee_name} is done with tasks ({task_done}/{total_task})")

        """Title of completed tasks"""
        for task in tasks_list:
            if task["completed"]:
                print(f"\t {task['task']}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: Script <employee_id>")
    else:
        get_employee_todos_progress(argv[1])

