import pandas as pd

def iloc_selection(data, row, col):
    df = pd.DataFrame(data)
    return [ df.iloc[row,col], df.iloc[row,:].tolist(), df.iloc[:, col].tolist()]