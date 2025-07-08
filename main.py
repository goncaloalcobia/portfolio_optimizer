# portfolio_optimizer/main.py

from src.data_loader import load_data
from src.optimizer import optimize_portfolio
from src.backtest import backtest_portfolio
from src.plots import plot_efficient_frontier

# === CONFIG ===
TICKERS = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "BTC-USD"]
START = "2020-01-01"
END = "2025-01-01"
METHOD = "sharpe"  # Options: 'sharpe', 'min_volatility', 'cvar'
BACKTEST = True # Set to False to skip backtesting

# === PIPELINE ===
if __name__ == "__main__":
    data = load_data(tickers=TICKERS, start=START, end=END)
    weights, performance = optimize_portfolio(data, method=METHOD)

    print("\nOptimal Weights:")
    for ticker, w in weights.items():
        print(f"{ticker}: {w:.2%}")

    print("\nPerformance Metrics:")
    for k, v in performance.items():
        print(f"{k}: {v:.2f}")

    plot_efficient_frontier(data, method=METHOD, highlight_weights=weights)

    if BACKTEST:
        print("\nStarting backtest...")
        backtest_portfolio(data, weights)
