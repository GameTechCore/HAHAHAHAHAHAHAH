# invoices.py

import pandas as pd

# Load invoice data from the CSV file
invoices_df = pd.read_csv('invoices.csv')

def generate_invoice(project_id, client_id, amount, due_date):
    """
    Generate a new invoice for a project and client.

    Args:
    - project_id: Project ID
    - client_id: Client ID
    - amount: Invoice amount
    - due_date: Due date for the invoice

    Returns:
    - None
    """
    new_invoice = pd.DataFrame({'Project ID': [project_id], 'Client ID': [client_id], 'Amount': [amount], 'Due Date': [due_date]})
    invoices_df = invoices_df.append(new_invoice, ignore_index=True)
    invoices_df.to_csv('../data/invoices.csv', index=False)
    print(f"Invoice for Project {project_id} generated successfully.")

def list_invoices():
    """
    List all invoices in the invoice records.

    Returns:
    - None
    """
    print("List of Invoices:")
    print(invoices_df)

# Example usage
if __name__ == "__main__":
    print("Invoices Module Example")
    generate_invoice(201, 301, 5000, "2023-03-15")
    generate_invoice(202, 302, 6000, "2023-03-31")
    list_invoices()
