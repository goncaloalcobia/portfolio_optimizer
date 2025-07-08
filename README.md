# 📈 Portfolio Optimizer

A Python-based quantitative finance project to build, optimize, and evaluate investment portfolios using expected returns, risk metrics, and strategies such as **Sharpe Ratio** or **Minimum Volatility**.

---

## 🚀 Features

✅ Fetches historical price data via [Yahoo Finance](https://finance.yahoo.com/)  
✅ Portfolio optimization using `PyPortfolioOpt` (Sharpe, minimum volatility)  
✅ Efficient Frontier visualization  
✅ Backtest simulation with periodic rebalancing  
✅ Computes metrics: expected return, volatility, Sharpe Ratio  

---

## 🧱 Project Structure

```text
portfolio_optimizer/
├── main.py              # Entry point
└── src/
    ├── data_loader.py   # Data loading and transformation
    ├── optimizer.py     # Optimization algorithms
    ├── backtest.py      # Portfolio performance simulation
    └── plots.py         # Visualizations
```

---

## ⚙️ Instalation
```bash
# Clone the repo
git clone git@github.com:goncaloalcobia/portfolio_optimizer.git
cd portfolio_optimizer

# Install dependencies
pip install -r requirements.txt
```

---

## 📈 Usage
```python
TICKERS = ["AAPL", "MSFT", "BTC-USD"]
START = "2020-01-01"
END = "2025-01-01"
METHOD = "sharpe"  # ou 'min_volatility'
```
Depois corre:
```bash
python main.py
```

---

## 🧠 Tech Stack
- Python 3.10+
- [PyPortfolioOpt](https://github.com/goncaloalcobia/PyPortfolioOpt)
- yfinance, matplotlib, pandas, numpy
- cvxpy para otimização

---

## 📜 License
NA.

