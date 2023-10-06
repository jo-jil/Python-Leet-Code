import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    pro = products.fillna(0)
    return pro
