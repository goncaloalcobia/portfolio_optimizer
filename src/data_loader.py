# src/data_loader.py

import yfinance as yf
import pandas as pd

def load_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end)["Adj Close"]
    data = data.dropna()
    return data

def calculate_returns(price_df):
    return price_df.pct_change().dropna()

