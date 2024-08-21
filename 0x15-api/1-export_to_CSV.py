#!/usr/bin/python3
"""Python script that, using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
import requests
from sys import argv

"""The modules to work with"""


def get_employee_todos_progress(employee_id):
    """A function about the employee todos progress to return the info"""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_datas = requests.get("{}users/{}".format(url, employee_id))
        user_data = user_datas.json()
        employee_name = user_data['username']

        """fetch the employee's todos list"""
        todos_list = requests.get("{}todos?userId={}".format(url, employee_id))
        json_todos_list = todos_list.json()

        total_task = len(json_todos_list)
        task_done = [task for task in json_todos_list if task['completed']]
        no_task_done = len(task_done) 

        """Display the result"""
        print("Employee {} is done with tasks ({}/{})".format(employee_name, no_task_done, total_task))

        """Title of completed task"""
        for task in task_done: 
            print("\t {}".format(task['title']))

	"""to export data in the CSV format"""
	csv_filename = "{}.csv".format(employee_id)
	with open(csv_filename, mode='w', newline='') as csv_file:
		writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
		for task in json_todos_list:
			 writer.writerow([employee_id, employee_name, task['completed'], task['title']])

    except Exception as e:
        print("An error occurred: {}".format(e))
    
    
if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: Script <employee_id>")
    else:
        get_employee_todos_progress(argv[1])
