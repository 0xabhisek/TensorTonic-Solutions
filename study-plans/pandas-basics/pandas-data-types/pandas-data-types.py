import pandas as pd

def data_types_overview(data):

    df = pd.DataFrame(data)
    dtypes = {col: str(dtype) for col,dtype in df.dtypes.items()}
    type_counts = {}

    for dtype in dtypes.values():
        type_counts[dtype] = type_counts.get(dtype, 0) + 1
    num_columns = df.shape[1]

    return {
        "dtypes": dtypes,
        "type_counts": type_counts,
        "num_columns": num_columns
    }