# src/plots.py

import matplotlib.pyplot as plt
from pypfopt import EfficientFrontier, risk_models, expected_returns, plotting

def plot_efficient_frontier(price_df, method="sharpe", highlight_weights=None):
    mu = expected_returns.mean_historical_return(price_df)
    S = risk_models.sample_cov(price_df)

    ef = EfficientFrontier(mu, S)
    fig, ax = plt.subplots(figsize=(8, 6))
    plotting.plot_efficient_frontier(ef, ax=ax, show_assets=True)

    if highlight_weights:
        ef_port = EfficientFrontier(mu, S)
        ef_port.set_weights(highlight_weights)
        ret, vol, _ = ef_port.portfolio_performance()
        ax.scatter(vol, ret, marker="*", color="r", s=100, label="Optimized Portfolio")

    ax.set_title("Efficient Frontier")
    ax.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

