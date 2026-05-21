import pandas as pd

def iloc_selection(data, row, col):
    """
    Returns: list [element, row_values, col_values]
    """
    df = pd.DataFrame(data)
    ele = df.iloc[row,col]
    rv = df.iloc[row,:].tolist()
    cv = df.iloc[:,col].tolist()
    return [ele,rv,cv]