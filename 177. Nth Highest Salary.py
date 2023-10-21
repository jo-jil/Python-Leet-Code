import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:    
    unique_salaries = employee['salary'].drop_duplicates()
    sorted_salaries = unique_salaries.sort_values(ascending=False)
    name = "getNthHighestSalary(" + str(N) + ")"
    if N > len(sorted_salaries):
        data = {name: [None]}
        df = pd.DataFrame(data)
    else:
        nth_highest = sorted_salaries.iloc[N - 1]
        return pd.DataFrame({name: [nth_highest]})
    return df
