import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """
    df = pd.DataFrame(data)
    ele = df.iloc[row,col]
    r = df.iloc[row,:]
    c = df.iloc[:,col]
    return [ele,r,c]