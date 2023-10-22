import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ids = orders['customerId'].tolist()
    filtered_df = customers[~customers['id'].isin(ids)][['name']]
    filtered_df = filtered_df.rename(columns={'name': 'Customers'})
    return filtered_df
