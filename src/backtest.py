# src/backtest.py

import pandas as pd
import matplotlib.pyplot as plt

def backtest_portfolio(price_data, weights):
    """
    Simula o valor acumulado de uma carteira com pesos fixos ao longo do tempo.
    """
    # Calcular retornos diários
    returns = price_data.pct_change().dropna()

    # Garantir que os pesos estão normalizados
    weights = pd.Series(weights)
    weights = weights / weights.sum()

    # Calcular o retorno diário da carteira
    portfolio_returns = (returns * weights).sum(axis=1)

    # Valor acumulado da carteira (começando com 100)
    cumulative_returns = (1 + portfolio_returns).cumprod() * 100

    # Plot
    plt.figure(figsize=(10, 5))
    plt.plot(cumulative_returns, label="Portfolio")
    plt.title("Backtest: Portfolio Cumulative Returns")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()
