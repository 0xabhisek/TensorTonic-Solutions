import pandas as pd

def drop_duplicates(data):
    """
    Returns: list [rows_before, rows_after, cleaned_data]
    """
    df = pd.DataFrame(data)
    rb = df.shape[0]
    df = df.drop_duplicates()
    ra= df.shape[0]
    return [rb,ra, df.to_dict('list')]
    