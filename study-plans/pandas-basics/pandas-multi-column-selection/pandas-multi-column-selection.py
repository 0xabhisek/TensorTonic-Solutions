import pandas as pd

def select_columns(data, columns):
    """
    Returns: dict mapping selected column names to value lists
    """ 
    df = pd.DataFrame(data)
    filter = df[[col for col in columns]]
    return filter.to_dict('list')