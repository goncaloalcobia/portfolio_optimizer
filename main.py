from src.data_loader import load_data
from src.optimizer import optimize_portfolio
from src.backtest import backtest_portfolio
from src.plots import plot_efficient_frontier
from src.MonteCarlo import monte_carlo_simulation
from pypfopt import expected_returns, risk_models
import numpy as np

# === CONFIG ===
TICKERS = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA", "PLTR", "META", "NFLX", "AMD"]  
TRAIN_START = "2020-01-01"
TRAIN_END = "2023-12-31"
TEST_START = "2024-01-01"
TEST_END = "2025-01-01"
METHOD = "quadratic_utility" # Options: 'sharpe', 'min_volatility', 'efficient_risk', 'efficient_return'
RISK_AVERSION = 5.0  
BACKTEST = True  # Set to False to skip backtesting
USE_MONTE_CARLO = False  # Set to True to use Monte Carlo simulation for optimization


# === PIPELINE ===
if __name__ == "__main__":
    # Carregar dados para treino e teste
    train_data = load_data(tickers=TICKERS, start=TRAIN_START, end=TRAIN_END)
    test_data = load_data(tickers=TICKERS, start=TEST_START, end=TEST_END)

    # Otimização no período de treino
    #weights, performance = optimize_portfolio(train_data, method=METHOD)
    weights, performance = optimize_portfolio(train_data, method=METHOD, use_monte_carlo=USE_MONTE_CARLO, risk_aversion=RISK_AVERSION)


    print("\nOptimal Weights (treino):")
    for ticker, w in weights.items():
        print(f"{ticker}: {w:.2%}")

    print("\nPerformance Metrics (treino):")
    for k, v in performance.items():
        print(f"{k}: {v:.2f}")

    # Plot da fronteira eficiente
    plot_efficient_frontier(train_data, method=METHOD, highlight_weights=weights)

    # Simulação de Monte Carlo
    mu = expected_returns.mean_historical_return(train_data).values
    cov = risk_models.sample_cov(train_data).values
    w_array = np.array([weights[ticker] for ticker in train_data.columns])
    monte_carlo_simulation(mu, cov, w_array)

    # Backtest no período de teste
    if BACKTEST:
        print("\nStarting backtest (teste)...")
        backtest_portfolio(test_data, weights)