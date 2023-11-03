# projects.py

import pandas as pd

# Load project data from the CSV file
projects_df = pd.read_csv('projects.csv')

def add_project(project_id, name, client, start_date, end_date):
    """
    Add a new project to the project database.

    Args:
    - project_id: Project ID
    - name: Project name
    - client: Client name or ID
    - start_date: Project start date
    - end_date: Project end date

    Returns:
    - None
    """
    new_project = pd.DataFrame({'Project ID': [project_id], 'Name': [name], 'Client': [client], 'Start Date': [start_date], 'End Date': [end_date]})
    projects_df = projects_df.append(new_project, ignore_index=True)
    projects_df.to_csv('../data/projects.csv', index=False)
    print(f"Project '{name}' added successfully.")

def list_projects():
    """
    List all projects in the project database.

    Returns:
    - None
    """
    print("List of Projects:")
    print(projects_df)

# Example usage
if __name__ == "__main__":
    print("Projects Module Example")
    add_project(201, "Software Upgrade", "ABC Corp", "2023-01-15", "2023-04-30")
    add_project(202, "Mobile App Development", "XYZ Inc", "2023-02-20", "2023-06-30")
    list_projects()
