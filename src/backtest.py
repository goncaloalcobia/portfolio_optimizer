# src/backtest.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def backtest_portfolio(price_df, weights, rebalance_period="M"):
    returns = price_df.pct_change().dropna()
    weights_series = pd.Series(weights)

    # Normalize and resample
    resampled_prices = price_df.resample(rebalance_period).last()
    resampled_returns = resampled_prices.pct_change().dropna()

    weighted_returns = (resampled_returns * weights_series).sum(axis=1)
    cumulative = (1 + weighted_returns).cumprod()

    plt.figure(figsize=(10, 5))
    plt.plot(cumulative, label="Backtest Portfolio")
    plt.title("Portfolio Backtest")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Return")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

