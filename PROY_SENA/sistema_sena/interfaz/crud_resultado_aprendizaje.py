import tkinter as tk
from tabulate import tabulate

root = tk.Tk()
root.geometry("400x300")
root.title("Tabla con Tkinter y Tabulate")

# Datos para la tabla
data = [
    ["Nombre", "Edad", "Ciudad"],
    ["Juan", 30, "Madrid"],
    ["María", 25, "Barcelona"],
    ["Pedro", 40, "Valencia"]
]

# Generar la tabla usando tabulate
tabla_texto = tabulate(data, headers="firstrow", tablefmt="grid")

# Crear un widget Text para mostrar la tabla
tabla_text = tk.Text(root, font=("Courier", 10))
tabla_text.insert(tk.END, tabla_texto)
tabla_text.pack(padx=10, pady=10)

root.mainloop()
