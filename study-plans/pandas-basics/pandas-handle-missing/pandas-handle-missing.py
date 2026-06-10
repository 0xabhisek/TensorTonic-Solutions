import pandas as pd

def handle_missing(data, fill_value):
    """
    Returns: dict with 'null_counts' (dict) and 'cleaned_data' (dict)
    """
    df = pd.DataFrame(data)
    nc = df.isnull().sum().to_dict()
    f = df.fillna(fill_value).to_dict('list')
    return {
        "null_counts": nc,
        "cleaned_data": f
    }