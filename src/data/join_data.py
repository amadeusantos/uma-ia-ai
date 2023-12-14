import pandas as pd
import glob

def data_append():
    files = glob.glob('data/raw/*.gzip')
    list_dfs = []
    for file in files:
        df = pd.read_parquet(file)
        list_dfs.append(df)
    df_appended = pd.concat(list_dfs, ignore_index=True)
    df_appended.to_parquet(path='data/processed/df_appended.parquet.gzip', compression='gzip')

data_append()
