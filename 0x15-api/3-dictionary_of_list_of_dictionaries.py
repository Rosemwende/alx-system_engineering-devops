#!/usr/bin/python3
"""Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv
from urllib.parse import urljoin

def get_employee_todos_progress(employee_id):
    """Fetch and display the TODO list progress for a given employee ID."""
    base_url = "https://jsonplaceholder.typicode.com/"
    try:
        """Fetch user data"""
        user_url = urljoin(base_url, f"users/{employee_id}")
        user_data = requests.get(user_url).json()
        employee_name = user_data.get('name', 'Unknown Employee')

        """Fetch todos list"""
        todos_url = urljoin(base_url, f"todos?userId={employee_id}")
        todos_list = requests.get(todos_url).json()

        total_task = len(todos_list)
        task_done = [task for task in todos_list if task.get('completed', False)]
        no_task_done = len(task_done)

        """Display results"""
        print(f"Employee {employee_name} is done with tasks ({no_task_done}/{total_task})")

        """Print titles of completed tasks"""
        for task in task_done:
            print(f"\t {task.get('title', 'No Title')}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred with the request: {e}")
    except KeyError as e:
        print(f"Missing key in response data: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: script <employee_id>")
    else:
        try:
            employee_id = int(argv[1])
            get_employee_todos_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer for employee ID.")

