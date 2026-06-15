import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    df = pd.DataFrame(data)
    v = df[column].tolist()
    l = int(len(v))
    return{'values': v, 'length': l}