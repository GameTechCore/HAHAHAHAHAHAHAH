# financials.py

import pandas as pd

# Load financial data from the CSV file
financials_df = pd.read_csv('financials.csv')

def add_financial_entry(date, revenue, expenses, net_profit):
    """
    Add a new financial entry to the financial records.

    Args:
    - date: Date of the financial entry
    - revenue: Revenue for the entry
    - expenses: Expenses for the entry
    - net_profit: Net profit for the entry

    Returns:
    - None
    """
    new_entry = pd.DataFrame({'Date': [date], 'Revenue': [revenue], 'Expenses': [expenses], 'Net Profit': [net_profit]})
    financials_df = financials_df.append(new_entry, ignore_index=True)
    financials_df.to_csv('../data/financials.csv', index=False)
    print(f"Financial entry for {date} added successfully.")

def list_financial_entries():
    """
    List all financial entries in the financial records.

    Returns:
    - None
    """
    print("List of Financial Entries:")
    print(financials_df)

# Example usage
if __name__ == "__main__":
    print("Financials Module Example")
    add_financial_entry("2023-01-01", 10000, 5000, 5000)
    add_financial_entry("2023-02-01", 12000, 6000, 6000)
    list_financial_entries()
