import yfinance as yf
import pandas as pd

def download_data(symbols: list, start_date: str, end_date: str):
    lista_dfs = []
    path = 'data/raw/'
    for symbol in symbols:
        df = yf.download(symbol, start=start_date, end=end_date)
        df['Name'] = symbol
        path_full = path + symbol + '.parquet.gzip'
        if df.shape[0] == 0:
            print(f"A base {symbol} não está disponivel ")
        else:
            df.to_parquet(path_full, compression='gzip')


symbols = ['BTC-USD', 'ETH-USD', 'USDT-USD', 'SOL-USD', 'DOGE-USD']
start_date = '2018-01-01'
end_date = '2023-11-29'

download_data(symbols, start_date, end_date)