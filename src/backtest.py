# src/backtest.py

import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

def backtest_portfolio(price_data, weights, benchmark_ticker="SPY"):
    # === Calcula retornos do portfólio ===
    daily_returns = price_data.pct_change().dropna()
    portfolio_returns = (daily_returns * pd.Series(weights)).sum(axis=1)
    cumulative_returns = (1 + portfolio_returns).cumprod() * 100  # Base 100

    # === Baixa e processa o benchmark ===
    benchmark_data = yf.download(benchmark_ticker, start=price_data.index[0], end=price_data.index[-1], auto_adjust=True)
    benchmark = benchmark_data["Close"]

    benchmark_returns = benchmark.pct_change().dropna()
    benchmark_cumulative = (1 + benchmark_returns).cumprod() * 100  # Base 100

    # === Plota ambos ===
    plt.figure(figsize=(14, 6))
    plt.plot(cumulative_returns.index, cumulative_returns, label="Optimized Portfolio", linewidth=2)
    plt.plot(benchmark_cumulative.index, benchmark_cumulative, label=f"Benchmark ({benchmark_ticker})", linestyle="--")
    plt.title("Backtest: Portfolio vs Benchmark")
    plt.xlabel("Date")
    plt.ylabel("Cumulative Returns (Base 100)")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
