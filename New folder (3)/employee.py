# employees.py

import pandas as pd

# Load employee data from CSV
employees_df = pd.read_csv('employees.csv')

# Function to add a new employee
def add_employee(employee_id, name, role):
    new_employee = pd.DataFrame({'Employee ID': [employee_id], 'Name': [name], 'Role': [role]})
    employees_df = employees_df.append(new_employee, ignore_index=True)
    employees_df.to_csv('employees.csv', index=False)
    list_employee()
# Function to list all employees
def list_employees():
    print("List of Employees:")
    print(employees_df)
employee_id=int(input())
name=input()
role=input()
add_employee()
