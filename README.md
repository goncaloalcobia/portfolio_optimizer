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
├── main.py              # Ponto de entrada
├── config.py            # Configuração do utilizador
└── src/
    ├── data_loader.py
    ├── optimizer.py
    ├── backtest.py
    ├── plots.py
    └── MonteCarlo.py    
```

---

## ⚙️ Instalation
```bash
# Clone the repo
git clone git@github.com:goncaloalcobia/portfolio_optimizer.git
cd portfolio_optimizer
```

### 🔧 Install dependencies with Python or Anaconda:

### a) With Python + pip
```bash
pip install -r requirements.txt
```

### b) With Anaconda (recommended)
```bash
# Create a new environment
conda create -n PO python=3.10 -y
conda activate PO

# Install pip inside conda
conda install pip -y

# Install requirements
pip install -r requirements.txt
```

---

## 📈 Usage

The portfolio configuration, date ranges, and optimization method are set in the `config.py`
```python
TICKERS = ["AAPL", "MSFT", "GOOG", "AMZN", "NVDA", "TSLA"]
TRAIN_START = "2020-01-01"
TRAIN_END = "2023-12-31"
TEST_START = "2024-01-01"
TEST_END = "2025-01-01"
METHOD = "sharpe"  # Options: 'sharpe', 'min_volatility', 'efficient_risk', 'efficient_return', 'quadratic_utility'
USE_MONTE_CARLO = False
BACKTEST = True
```
Simply modify the values in `config.py` to customize the optimization process without touching `main.py`. Then run:
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
This project is licensed under the [MIT License](LICENSE).