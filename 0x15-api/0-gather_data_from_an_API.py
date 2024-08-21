#!/usr/bin/python3
""" Python script that, using this REST API, 
 for a given employee ID, 
 returns information about his/her TODO list progress """

import requests
import sys

if __name__ == "__main__":
    """Check if the script receives the employee ID as an argument"""
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    
    """Define the API endpoints"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    
    """Fetch user information"""
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name")
    
    """Fetch todos information"""
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()
    
    """Calculate the number of done tasks and total tasks"""
    done_tasks = [task for task in todos_data if task.get("completed")]
    total_tasks = len(todos_data)
    number_of_done_tasks = len(done_tasks)
    
    """Print the employee's TODO list progress"""
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")
    
     """ Print the titles of completed tasks """
    for task in done_tasks:
        print(f"\t {task.get('title')}")
