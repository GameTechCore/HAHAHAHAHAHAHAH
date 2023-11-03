software_company_management/
    ├── data/
    │   ├── employees.csv
    │   ├── projects.csv
    │   ├── clients.csv
    │   ├── financials.csv
    │   ├── invoices.csv
    │   ├── tasks.csv
    ├── src/
    │   ├── __init__.py
    │   ├── employees.py
    │   ├── projects.py
    │   ├── clients.py
    │   ├── financials.py
    │   ├── invoices.py
    │   ├── tasks.py
    ├── main.py











# main.py

from src import employees, projects, clients, financials, invoices, tasks

while True:
    print("Software Company Management System")
    print("1. Manage Employees")
    print("2. Manage Projects")
    print("3. Manage Clients")
    print("4. Financial Reporting")
    print("5. Generate Invoice")
    print("6. Manage Tasks")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        employees.add_employee(employee_id, name, role)
    elif choice == '2':
        projects.manage_projects()
    elif choice == '3':
        clients.manage_clients()
    elif choice == '4':
        financials.financial_reporting()
    elif choice == '5':
        invoices.generate_invoice()
    elif choice == '6':
        tasks.manage_tasks()
    elif choice == '7':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
