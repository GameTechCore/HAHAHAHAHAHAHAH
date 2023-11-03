# tasks.py

import pandas as pd

# Load task data from the CSV file
tasks_df = pd.read_csv('tasks.csv')

def add_task(task_id, project_id, description, status):
    """
    Add a new task to the task database.

    Args:
    - task_id: Task ID
    - project_id: Project ID the task belongs to
    - description: Task description
    - status: Task status (e.g., "Open", "In Progress", "Completed")

    Returns:
    - None
    """
    new_task = pd.DataFrame({'Task ID': [task_id], 'Project ID': [project_id], 'Description': [description], 'Status': [status]})
    tasks_df = tasks_df.append(new_task, ignore_index=True)
    tasks_df.to_csv('../data/tasks.csv', index=False)
    print(f"Task '{description}' added successfully.")

def update_task_status(task_id, new_status):
    """
    Update the status of an existing task.

    Args:
    - task_id: Task ID to update
    - new_status: New task status

    Returns:
    - None
    """
    tasks_df.loc[tasks_df['Task ID'] == task_id, 'Status'] = new_status
    tasks_df.to_csv('../data/tasks.csv', index=False)
    print(f"Task ID {task_id} status updated to '{new_status}'.")

def list_tasks():
    """
    List all tasks in the task database.

    Returns:
    - None
    """
    print("List of Tasks:")
    print(tasks_df)

# Example usage
if __name__ == "__main__":
    print("Tasks Module Example")
    add_task(301, 201, "Implement User Authentication", "Open")
    add_task(302, 201, "Design User Interface", "In Progress")
    update_task_status(301, "Completed")
    list_tasks()
