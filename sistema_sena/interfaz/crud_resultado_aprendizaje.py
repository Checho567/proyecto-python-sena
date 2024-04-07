# import tkinter as tk
# from tabulate import tabulate

# root = tk.Tk()
# root.geometry("400x300")
# root.title("Tabla con Tkinter y Tabulate")

# # Datos para la tabla
# data = [
#     ["Nombre", "Edad", "Ciudad"],
#     ["Juan", 30, "Madrid"],
#     ["María", 25, "Barcelona"],
#     ["Pedro", 40, "Valencia"]
# ]

# # Generar la tabla usando tabulate
# tabla_texto = tabulate(data, headers="firstrow", tablefmt="grid")

# # Crear un widget Text para mostrar la tabla
# tabla_text = tk.Text(root, font=("Courier", 10))
# tabla_text.insert(tk.END, tabla_texto)
# tabla_text.pack(padx=10, pady=10)

# root.mainloop()
import tkinter as tk
from tkinter import ttk

class ScrollableApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Crear el contenedor principal
        container = tk.Frame(self)
        container.pack(fill='both', expand=True)

        # Crear el lienzo (canvas) con scrollbars
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient='vertical', command=canvas.yview)
        scrollbar.pack(side='right', fill='y')
        canvas.config(yscrollcommand=scrollbar.set)
        canvas.pack(side='left', fill='both', expand=True)

        # Configurar el canvas para que expanda el frame interior
        canvas_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=canvas_frame, anchor='nw')

        # Configurar el frame interior
        self.canvas_frame = canvas_frame
        canvas_frame.bind('<Configure>', lambda e: canvas.config(scrollregion=canvas.bbox('all')))

        # Agregar un widget de ejemplo al frame interior
        for i in range(50):
            tk.Label(canvas_frame, text=f"Label {i}").pack()

app = ScrollableApp()
app.mainloop()