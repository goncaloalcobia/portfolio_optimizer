# config.py

TICKERS = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "PLTR", "META", "NFLX", "AMD"]  

TRAIN_START = "2020-01-01"
TRAIN_END = "2023-12-31"
TEST_START = "2024-01-01"
TEST_END = "2025-01-01"

METHOD = "quadratic_utility" # Options: 'sharpe', 'min_volatility', 'efficient_risk', 'efficient_return'
BACKTEST = True
USE_MONTE_CARLO = False
RISK_AVERSION = 3.0  # Only used if method == "quadratic_utility"

