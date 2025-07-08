import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def monte_carlo_simulation(mu, cov, weights, n_simulations=500, n_days=252):

    portfolio_returns = []

    for _ in range(n_simulations):
        # Simula retornos diários multivariados
        daily_returns = np.random.multivariate_normal(mu / n_days, cov / n_days, n_days)
        # Calcula retorno diário do portfólio
        portfolio_daily_returns = np.dot(daily_returns, weights)
        # Acumula retorno total
        total_return = np.prod(1 + portfolio_daily_returns) - 1
        portfolio_returns.append(total_return)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.hist(portfolio_returns, bins=50, alpha=0.7, color='skyblue')
    plt.axvline(np.mean(portfolio_returns), color='red', linestyle='--', label=f"Mean Return: {np.mean(portfolio_returns):.2%}")
    plt.title("Monte Carlo Simulation of Portfolio Return")
    plt.xlabel("Total Return over 1 year")
    plt.ylabel("Frequency")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def estimate_mu_cov_via_monte_carlo(price_df, n_simulations=5000, horizon_days=252):
    log_returns = np.log(price_df / price_df.shift(1)).dropna().values
    mu_historical = log_returns.mean(axis=0)
    sigma_historical = np.cov(log_returns.T)

    n_assets = log_returns.shape[1]
    simulations = np.zeros((n_simulations, n_assets))

    for i in range(n_simulations):
        simulated_returns = np.random.multivariate_normal(mu_historical, sigma_historical, horizon_days)
        cumulative_returns = np.exp(simulated_returns.cumsum(axis=0))[-1]
        simulations[i] = cumulative_returns - 1

    mu_sim = simulations.mean(axis=0)
    cov_sim = np.cov(simulations.T)

    return pd.Series(mu_sim, index=price_df.columns), pd.DataFrame(cov_sim, index=price_df.columns, columns=price_df.columns)

