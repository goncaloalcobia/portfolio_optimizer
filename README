# Portfolio Optimizer 📊💼

Um projeto de análise quantitativa em Python que constrói, otimiza e avalia carteiras de investimento com base em retorno esperado, risco e diferentes estratégias como Sharpe ratio ou volatilidade mínima.

---

## 🚀 Funcionalidades
- Carregamento de preços históricos via Yahoo Finance
- Otimização da carteira com `PyPortfolioOpt` (Sharpe, mínima volatilidade)
- Visualização da fronteira eficiente
- Simulação de backtest com rebalanceamento periódico
- Cálculo de métricas como retorno esperado, volatilidade, Sharpe Ratio

---

## 📁 Estrutura
```
portfolio_optimizer/
├── main.py               # Ponto de entrada
└── src/
    ├── data_loader.py   # Carregamento e transformação de dados
    ├── optimizer.py     # Algoritmos de otimização
    ├── backtest.py      # Simulação de performance
    └── plots.py         # Visualizações
```

---

## ⚙️ Instalação
```bash
# Clona o repositório
git clone https://github.com/teu-username/portfolio_optimizer.git
cd portfolio_optimizer

# Cria ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# Instala dependências
pip install -r requirements.txt
```

---

## 📈 Uso
Edita os tickers e datas no `main.py`:
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

## 🧠 Tecnologias usadas
- Python 3.10+
- [PyPortfolioOpt](https://github.com/goncaloalcobia/PyPortfolioOpt)
- yfinance, matplotlib, pandas, numpy
- cvxpy para otimização

---

## 📜 Licença
Este projeto está licenciado sob a licença MIT.

