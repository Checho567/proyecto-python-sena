import tkinter as tk
from tkinter import messagebox
import sqlite3
from tabulate import tabulate

class CRUDCompetencia(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        # Dimensiones y titulo de la ventana
        self.geometry("550x350")
        self.title("Sistema Sena")

        # Titulo de la ventana
        self.titulo_inicio = tk.Label(self, text='Panel de competencias', font=('Arial', 22))
        self.titulo_inicio.grid(row=0, column=0, columnspan=3, pady=2)

        # label y caja de texto para crud de programa
        self.lbl_nombre_competencia = tk.Label(self, text='Nombre de la competencia: ', font=('Arial', 12))
        self.lbl_nombre_competencia.grid(row=1, column=0, pady=20)

        self.txt_nombre_competencia = tk.Entry(self, text="Nombre de la competencia", font=('Arial', 12), width=20)
        self.txt_nombre_competencia.grid(row=1, column=1, pady=20)

        # boton de crear competencia
        self.btn_crear_competencia = tk.Button(
            self, 
            text='Crear competencia', 
            font=('Arial', 12), 
            width=14, 
            bg='green', 
            fg="white"
        )
        self.btn_crear_competencia.grid(row=2, column=0, columnspan=1, pady=20)
        
        # Boton de editar competencia
        self.btn_editar_competencia = tk.Button(
            self, 
            text='Editar competencia', 
            font=('Arial', 12), 
            width=14, 
            bg='blue', 
            fg="white"
        )
        self.btn_editar_competencia.grid(row=2, column=1, columnspan=1, pady=20)
        
        # Boton de eliminar competencia
        self.btn_eliminar_competencia = tk.Button(
            self, 
            text='Eliminar competencia', 
            font=('Arial', 12), 
            width=14, 
            bg='red', 
            fg="white"
        )
        self.btn_eliminar_competencia.grid(row=2, column=2, columnspan=1, pady=20)
        
        # encabezados = [
        #     ["ID Programa", "Nombre de programa"]
        # ]
        # headers_tabla = tabulate(encabezados, headers="firstrow", tablefmt="fancy")
        
        # self.tabla_programa = tk.Label(
        #     self, 
        #     text=headers_tabla,
        #     font=('Arial', 12)
        #     )
        # self.tabla_programa.grid(row=3, column=0, pady=10)
        
        # self.lbl_id_programa

programa = CRUDCompetencia()
programa.mainloop()
