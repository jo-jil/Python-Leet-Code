import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    value_counts = employee['managerId'].value_counts()
    result = []
    # Filter the values that appear more than 5 times
    filtered_values = value_counts[value_counts >= 5].index.tolist()
    for i in filtered_values:
        result += employee.loc[employee['id'] == i, 'name'].tolist()
    ans = {'name': result}
    an = pd.DataFrame(ans)
    return an
