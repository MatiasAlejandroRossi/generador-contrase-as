import tkinter as tk
from tkinter import messagebox
import secrets
import string

def generar_contraseña(longitud=16, evitar_ambiguos=True):
    if longitud < 12:
        raise ValueError("La longitud mínima recomendada es 12 caracteres.")

    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    ambiguos = 'l1O0'

    conjunto = letras + numeros + simbolos
    if evitar_ambiguos:
        conjunto = ''.join(c for c in conjunto if c not in ambiguos)

    return ''.join(secrets.choice(conjunto) for _ in range(longitud))

def generar_y_mostrar():
    try:
        longitud = int(entry_longitud.get())
        evitar = var_ambiguos.get()
        contraseña = generar_contraseña(longitud, evitar)
        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, contraseña)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Interfaz
root = tk.Tk()
root.title("Generador de Contraseñas Seguras")
root.geometry("400x200")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Longitud de la contraseña:").pack(pady=5)
entry_longitud = tk.Entry(root)
entry_longitud.insert(0, "16")
entry_longitud.pack()

var_ambiguos = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Evitar caracteres ambiguos (l, 1, O, 0)", variable=var_ambiguos).pack(pady=5)

tk.Button(root, text="Generar contraseña", command=generar_y_mostrar).pack(pady=10)

entry_resultado = tk.Entry(root, width=40, font=("Courier", 12))
entry_resultado.pack(pady=5)

root.mainloop()