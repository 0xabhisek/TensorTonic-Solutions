import pandas as pd

def inspect_dataframe(data):
    """
    Returns: dict with 'rows', 'cols' (ints), 'columns' (list),
    'dtypes' (dict), 'total_values' (int)
    """
    df = pd.DataFrame(data)
    r = len(df)
    c = df.shape[1]
    col = df.columns.tolist()
    dt = {c : str(dtype) for c,dtype in df.dtypes.items()}
    tv = r*c
    return { 'rows': r, 'cols': c, 'columns': col, 'dtypes': dt, 'total_values': tv}