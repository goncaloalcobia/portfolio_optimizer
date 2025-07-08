# src/data_loader.py

import yfinance as yf
import pandas as pd

def load_data(tickers, start, end):
    raw_data = yf.download(tickers, start=start, end=end, group_by='ticker', auto_adjust=True)
    data = pd.DataFrame({ticker: raw_data[ticker]["Close"] for ticker in tickers})
    data = data.dropna()
    return data

def calculate_returns(price_df):
    return price_df.pct_change().dropna()
