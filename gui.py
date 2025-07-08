import tkinter as tk
from tkinter import messagebox
import subprocess

# === Modo default com tickers predefinidos ===
DEFAULT = True
DEFAULT_TICKERS = ['AAPL', 'MSFT', 'GOOG', 'AMZN', 'NVDA', 'TSLA', 'PLTR', 'META', 'NFLX', 'AMD']

tickers = []

def update_ticker_fields():
    for widget in ticker_frame.winfo_children():
        widget.destroy()
    tickers.clear()

    if DEFAULT:
        entries = DEFAULT_TICKERS
    else:
        try:
            n = int(num_tickers_entry.get())
            entries = [""] * n
            entries[0] = "AAPL"  # exemplo
        except ValueError:
            messagebox.showerror("Erro", "Número de ações inválido")
            return

    for i, val in enumerate(entries):
        tk.Label(ticker_frame, text=f"Ticker {i+1}:").grid(row=i, column=0, sticky="w")
        entry = tk.Entry(ticker_frame)
        entry.insert(0, val)
        entry.grid(row=i, column=1)
        tickers.append(entry)

def run_optimization():
    try:
        ticker_list = [e.get().strip().upper() for e in tickers if e.get().strip()]
        if not ticker_list:
            raise ValueError("Pelo menos um ticker é necessário.")

        train_start = train_start_entry.get()
        train_end = train_end_entry.get()
        test_start = test_start_entry.get()
        test_end = test_end_entry.get()
        method = method_var.get()
        backtest = backtest_var.get()
        use_monte_carlo = mc_var.get()
        risk_aversion = float(risk_aversion_entry.get())

        with open("config.py", "w") as f:
            f.write("TICKERS = " + str(ticker_list) + "\n")
            f.write(f'TRAIN_START = "{train_start}"\n')
            f.write(f'TRAIN_END = "{train_end}"\n')
            f.write(f'TEST_START = "{test_start}"\n')
            f.write(f'TEST_END = "{test_end}"\n')
            f.write(f'METHOD = "{method}"\n')
            f.write(f'BACKTEST = {backtest}\n')
            f.write(f'USE_MONTE_CARLO = {use_monte_carlo}\n')
            f.write(f'RISK_AVERSION = {risk_aversion}\n')

        subprocess.run(["python", "main.py"])
    except Exception as e:
        messagebox.showerror("Erro", str(e))


# GUI
root = tk.Tk()
root.title("Portfolio Optimizer")

if not DEFAULT:
    tk.Label(root, text="Number of Tickers:").grid(row=0, column=0, sticky="w")
    num_tickers_entry = tk.Entry(root)
    num_tickers_entry.insert(0, "10")
    num_tickers_entry.grid(row=0, column=1)

    tk.Button(root, text="Update Ticker Fields", command=update_ticker_fields).grid(row=0, column=2, padx=5)

ticker_frame = tk.Frame(root)
ticker_frame.grid(row=1, column=0, columnspan=3, pady=5)

# Outros campos
tk.Label(root, text="Train Start:").grid(row=2, column=0, sticky="w")
train_start_entry = tk.Entry(root)
train_start_entry.insert(0, "2020-01-01")
train_start_entry.grid(row=2, column=1)

tk.Label(root, text="Train End:").grid(row=3, column=0, sticky="w")
train_end_entry = tk.Entry(root)
train_end_entry.insert(0, "2023-12-31")
train_end_entry.grid(row=3, column=1)

tk.Label(root, text="Test Start:").grid(row=4, column=0, sticky="w")
test_start_entry = tk.Entry(root)
test_start_entry.insert(0, "2024-01-01")
test_start_entry.grid(row=4, column=1)

tk.Label(root, text="Test End:").grid(row=5, column=0, sticky="w")
test_end_entry = tk.Entry(root)
test_end_entry.insert(0, "2025-01-01")
test_end_entry.grid(row=5, column=1)

tk.Label(root, text="Optimization Method:").grid(row=6, column=0, sticky="w")
method_var = tk.StringVar(root)
method_var.set("quadratic_utility")
method_menu = tk.OptionMenu(root, method_var, "sharpe", "min_volatility", "efficient_risk", "efficient_return", "quadratic_utility")
method_menu.grid(row=6, column=1, sticky="w")

backtest_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Enable Backtest", variable=backtest_var).grid(row=7, column=1, sticky="w")

mc_var = tk.BooleanVar(value=False)
tk.Checkbutton(root, text="Use Monte Carlo", variable=mc_var).grid(row=8, column=1, sticky="w")

tk.Label(root, text="Risk Aversion (only for quadratic_utility):").grid(row=9, column=0, sticky="w")
risk_aversion_entry = tk.Entry(root)
risk_aversion_entry.insert(0, "3.0")
risk_aversion_entry.grid(row=9, column=1)

tk.Button(root, text="Run Optimization", command=run_optimization, bg="green", fg="white").grid(row=10, column=1, pady=10)

# Inicializa tickers
update_ticker_fields()

root.mainloop()
