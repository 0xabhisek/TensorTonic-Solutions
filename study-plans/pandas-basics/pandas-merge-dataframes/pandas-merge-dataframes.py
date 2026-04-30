import pandas as pd

def merge_dataframes(left, right, on, how):
    """
    Returns: dict of column to value lists
    """
    df1 = pd.DataFrame(left)
    df2 = pd.DataFrame(right)
    r = pd.merge(df1,df2, on = on, how = how)
    return r.to_dict('list')