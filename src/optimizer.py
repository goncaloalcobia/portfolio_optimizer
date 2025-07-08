# src/optimizer.py

from pypfopt import EfficientFrontier, risk_models, expected_returns


def optimize_portfolio(price_df, method="sharpe"):
    mu = expected_returns.mean_historical_return(price_df)
    S = risk_models.sample_cov(price_df)

    ef = EfficientFrontier(mu, S)
    if method == "sharpe":
        weights = ef.max_sharpe()
    elif method == "min_volatility":
        weights = ef.min_volatility()
    else:
        raise NotImplementedError("Only 'sharpe' and 'min_volatility' supported yet")

    cleaned_weights = ef.clean_weights()
    performance = ef.portfolio_performance(verbose=False)

    return cleaned_weights, {
        "Expected Return": performance[0],
        "Volatility": performance[1],
        "Sharpe Ratio": performance[2]
    }

