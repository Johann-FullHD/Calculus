import ttkthemes
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle

def on_click(button_text):
    current_text = entry.get()
    new_text = current_text + button_text
    entry.delete(0, tk.END)
    entry.insert(0, new_text)

def clear_entry():
    entry.delete(0, tk.END)
    last_action_label.config(text="Letzte Aktion:")

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
        last_action_label.config(text=f'Letzte Aktion: {expression} = {result}', fg='green')
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Fehler")
        last_action_label.config(text='Letzte Aktion: Fehler', fg='red')

# GUI
root = tk.Tk()
root.title("Calculus")
root.geometry("400x500")
root.maxsize(400, 500)
root.minsize(250, 350)
root.configure(bg='#282c34')

# Stil für Fensterleiste
style = ThemedStyle(root)
style.set_theme("equilux")  

# Label für die letzte Aktion
last_action_label = tk.Label(root, text="Letzte Aktion:", font=("Helvetica", 12), bg='#282c34', fg='white')
last_action_label.grid(row=0, column=0, columnspan=4, pady=5, padx=10, sticky="nsew")

# Eingabefeld
entry = tk.Entry(root, width=20, font=("Helvetica", 16), justify="right", bd=10)
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="nsew")  # sticky="nsew" für Streckung

# Stil für Schaltflächen
style = ttk.Style()
style.configure("TButton", padding=10, font=("Helvetica", 14,), background='#FFFFFF', foreground='white')
style.map("TButton", background=[('pressed', '#228be6'), ('active', '#4b7bec')])

# Schaltflächen für Zahlen und Operationen
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    ttk.Button(root, text=button, style="TButton", command=lambda b=button: on_click(b) if b != '=' else calculate()).grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Schaltfläche zum Löschen der Eingabe
ttk.Button(root, text="Clear", style="TButton", command=clear_entry).grid(row=row_val, column=col_val, columnspan=4, padx=5, pady=5, sticky="nsew")

# Anpassung der Spalten und Zeilen beim Verschieben des Fensters
for i in range(4):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i + 1, weight=1)

# GUI starten
root.mainloop()