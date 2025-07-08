# src/optimizer.py

from src.MonteCarlo import estimate_mu_cov_via_monte_carlo
from pypfopt import EfficientFrontier, risk_models, expected_returns, objective_functions
import cvxpy as cp
cp.settings.SOLVER = "SCS"
cp.settings.EPS = 1e-8 

def optimize_portfolio(price_df, method="sharpe", target_value=0.27, use_monte_carlo=False, target_return=0.27, risk_aversion=3):
    if use_monte_carlo:
        mu, S = estimate_mu_cov_via_monte_carlo(price_df)
    else:
        mu = expected_returns.ema_historical_return(price_df, span=180)
        S = risk_models.CovarianceShrinkage(price_df).ledoit_wolf()


    ef = EfficientFrontier(mu, S)

    # === Restrições realistas ===
    ef.add_constraint(lambda w: w >= 0)        # Sem posições curtas
    ef.add_constraint(lambda w: w <= 0.3)      # Max 30% por ativo
    ef.add_objective(objective_functions.L2_reg, gamma=0.1)  # Penaliza pesos extremos
    ef.add_constraint(lambda w: w.sum() >= 0.98)
    ef.add_constraint(lambda w: w.sum() <= 1.0)

    # === Otimização por método ===
    if method == "sharpe":
        weights = ef.max_sharpe()
    elif method == "min_volatility":
        weights = ef.min_volatility()
    elif method == "efficient_risk":
        weights = ef.efficient_risk(target_volatility=target_value or 0.27)
    elif method == "efficient_return":
        weights = ef.efficient_return(target_return=target_value or 0.27)
    elif method == "quadratic_utility":
        risk_aversion = target_value or 3  # λ padrão se não for fornecido
        weights = ef.max_quadratic_utility(risk_aversion=risk_aversion)


    else:
        raise NotImplementedError("Método não suportado: usa 'sharpe', 'min_volatility', 'efficient_risk' ou 'efficient_return'")


    cleaned_weights = ef.clean_weights()
    performance = ef.portfolio_performance(verbose=False)

    return cleaned_weights, {
        "Expected Return": performance[0],
        "Volatility": performance[1],
        "Sharpe Ratio": performance[2]
    }
