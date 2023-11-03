# clients.py

import pandas as pd

# Load client data from the CSV file
clients_df = pd.read_csv('clients.csv')

def add_client(client_id, name, contact_name, contact_email, contact_phone):
    """
    Add a new client to the client database.

    Args:
    - client_id: Client ID
    - name: Client name
    - contact_name: Contact person's name
    - contact_email: Contact person's email
    - contact_phone: Contact person's phone number

    Returns:
    - None
    """
    new_client = pd.DataFrame({'Client ID': [client_id], 'Name': [name], 'Contact Name': [contact_name], 'Contact Email': [contact_email], 'Contact Phone': [contact_phone]})
    clients_df = clients_df.append(new_client, ignore_index=True)
    clients_df.to_csv('../data/clients.csv', index=False)
    print(f"Client '{name}' added successfully.")

def list_clients():
    """
    List all clients in the client database.

    Returns:
    - None
    """
    print("List of Clients:")
    print(clients_df)

# Example usage
if __name__ == "__main__":
    print("Clients Module Example")
    add_client(301, "ABC Corp", "John Smith", "john@abccorp.com", "+1 123-456-7890")
    add_client(302, "XYZ Inc", "Jane Doe", "jane@xyzinc.com", "+1 987-654-3210")
    list_clients()
