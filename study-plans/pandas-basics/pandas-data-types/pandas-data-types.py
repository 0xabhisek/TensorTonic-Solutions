import pandas as pd

def data_types_overview(data):
    df = pd.DataFrame(data)

    dtypes = {}
    type_counts = {}

    for col, dtype in df.dtypes.items():
        dtype_str = str(dtype)

        dtypes[col] = dtype_str
        type_counts[dtype_str] = type_counts.get(dtype_str, 0) + 1

    return {
        "dtypes": dtypes,
        "type_counts": type_counts,
        "num_columns": len(df.columns)
    }