import pandas as pd

def handle_missing(data, fill_value):
    """
    Returns: dict with 'null_counts' (dict) and 'cleaned_data' (dict)
    """
    df = pd.DataFrame(data)
    nc = {k: int(v) for k,v in df.isnull().sum().items()}
    df = df.fillna(fill_value)

    return {
        'null_counts': nc,
        'cleaned_data': df.to_dict('list')
    }