from config import (
    TICKERS, TRAIN_START, TRAIN_END, TEST_START, TEST_END,
    METHOD, BACKTEST, USE_MONTE_CARLO, RISK_AVERSION
)
from src.data_loader import load_data
from src.optimizer import optimize_portfolio
from src.backtest import backtest_portfolio
from src.plots import plot_efficient_frontier
from src.MonteCarlo import monte_carlo_simulation
from pypfopt import expected_returns, risk_models
import numpy as np

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