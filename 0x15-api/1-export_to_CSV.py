#!/usr/bin/env python3
"""Using what you did in the task #0,
extend your Python script to export data in the CSV format
"""

import requests
import csv
import sys

if __name__ == "__main__":
    """Get the employee ID from the command line arguments"""
    employee_id = sys.argv[1]
    
    """Base URL of the API"""
    url = "https://jsonplaceholder.typicode.com/"
    
    """Fetch user data"""
    user_data = requests.get(url + "users/{}".format(employee_id)).json()
    employee_name = user_data.get("username")
    
    """Fetch the todo list for the employee"""
    todos = requests.get(url + "todos?userId={}".format(employee_id)).json()
    
    """Specify the CSV file name"""
    filename = "{}.csv".format(employee_id)
    
    """Write the data to a CSV file"""
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id, employee_name, task.get("completed"), task.get("title")])
    
    print("Data exported to {}.csv".format(employee_id))
