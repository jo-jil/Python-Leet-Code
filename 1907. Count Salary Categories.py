import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = accounts[(accounts['income'] >= 0) & (accounts['income'] < 20000)]['income'].count()
    avg = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)]['income'].count()
    high = accounts[(accounts['income'] > 50000)]['income'].count()


    data = {
    'category': ['Low Salary', 'Average Salary', 'High Salary'],
    'accounts_count': [low, avg, high]
    }

    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)

    return df
