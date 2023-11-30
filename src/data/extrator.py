import yfinance as yf
import pandas as pd

def download_data(symbols: list, start_date: string, end_date: string):
    lista_dfs = []
    path = '../../data/raw/'
    for symbol in symbols:
        path_full = path + symbol + '.parquet.gzip'
        try:
            df = yf.download(symbol, start=start_date, end=end_date)
            df.to_parquet(path=path_full, compression='gzip')
        except:
            print("Erro no download")