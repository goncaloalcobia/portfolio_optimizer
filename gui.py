# gui.py

import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Button
from datetime import datetime
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
import io

from src.data_loader import load_data
from src.optimizer import optimize_portfolio
from src.plots import plot_efficient_frontier
from src.backtest import backtest_portfolio

def run_optimizer():
    tickers = ticker_entry.get().strip().upper().split()
    start_date = start_entry.get().strip()
    end_date = end_entry.get().strip()
    method = method_var.get()
    do_backtest = backtest_var.get()

    try:
        data = load_data(tickers, start=start_date, end=end_date)
        weights, ef = optimize_portfolio(data, method=method)

        # Cria novo gráfico e guarda como imagem em memória
        fig = plot_efficient_frontier(data, weights, ef)  # Removido show=False
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        img = Image.open(buf)
        photo = ImageTk.PhotoImage(img)

        # Nova janela
        result_window = Toplevel(root)
        result_window.title("Portfolio Results")

        # Mostra imagem
        label_img = Label(result_window, image=photo)
        label_img.image = photo  # manter referência
        label_img.pack()

        # Mostra alocações
        allocation_text = "\n".join([f"{k}: {round(v * 100, 2)}%" for k, v in weights.items()])
        Label(result_window, text=allocation_text, font=("Arial", 12), pady=10).pack()

        # Backtest
        if do_backtest:
            backtest_portfolio(data, weights)

        # Botão de voltar
        Button(result_window, text="Fechar", command=result_window.destroy).pack(pady=10)

    except Exception as e:
        messagebox.showerror("Erro", str(e))



# GUI
root = tk.Tk()
root.title("Portfolio Optimizer")

tk.Label(root, text="Tickers (separados por espaço):").grid(row=0, column=0, sticky='w')
ticker_entry = tk.Entry(root, width=50)
ticker_entry.grid(row=0, column=1)

tk.Label(root, text="Start Date (YYYY-MM-DD):").grid(row=1, column=0, sticky='w')
start_entry = tk.Entry(root)
start_entry.grid(row=1, column=1)

tk.Label(root, text="End Date (YYYY-MM-DD):").grid(row=2, column=0, sticky='w')
end_entry = tk.Entry(root)
end_entry.grid(row=2, column=1)

tk.Label(root, text="Optimization Method:").grid(row=3, column=0, sticky='w')
method_var = tk.StringVar(value="sharpe")
tk.OptionMenu(root, method_var, "sharpe", "min_volatility").grid(row=3, column=1, sticky='w')

backtest_var = tk.BooleanVar()
tk.Checkbutton(root, text="Run backtest after optimization", variable=backtest_var).grid(row=4, column=1, sticky='w')

tk.Button(root, text="Run Optimizer", command=run_optimizer, bg="green", fg="white").grid(row=5, column=1, pady=10)

root.mainloop()

