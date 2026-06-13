import pandas as pd

def reset_index_demo(data, index_col):
    """
    Returns: list [columns_before_reset, columns_after_reset]
    """
    df = pd.DataFrame(data)
    df = df.set_index(index_col)
    c1 = df.columns.tolist()
    df = df.reset_index()
    c2 = df.columns.tolist()
    return [c1,c2]