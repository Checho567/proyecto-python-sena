import tkinter as tk
from tkinter import messagebox
import sqlite3

class CRUDCompetencia(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        # Dimensiones y titulo de la ventana
        self.geometry("550x550")
        self.title("Sistema Sena")

        # Titulo de la ventana
        self.titulo_inicio = tk.Label(self, text='Panel de competencias', font=('Arial', 22))
        self.titulo_inicio.grid(row=0, column=0, columnspan=3, pady=2)

        # label y caja de texto para nombre de competencia
        self.lbl_nombre_competencia = tk.Label(self, text='Nombre de la competencia: ', font=('Arial', 12))
        self.lbl_nombre_competencia.grid(row=1, column=0, pady=20)
        self.txt_nombre_competencia = tk.Entry(self, text="Nombre de la competencia", font=('Arial', 12), width=20)
        self.txt_nombre_competencia.grid(row=1, column=1, pady=20)
        
        # label y caja de texto para programa
        self.lbl_programa = tk.Label(self, text='Programa: ', font=('Arial', 12))
        self.lbl_programa.grid(row=2, column=0, pady=10)
        self.lista_programa = tk.Listbox(self, font=('Arial', 12), selectmode=tk.SINGLE, height=5)
        self.lista_programa.grid(row=2, column=1, pady=10)
        
        # Label y caja de texto para resultado de aprendizaje
        self.lbl_resultado = tk.Label(self, text='Resultado de aprendizaje: ', font=('Arial', 12))
        self.lbl_resultado.grid(row=3, column=0, pady=10)
        self.lista_resultado = tk.Listbox(self, font=('Arial', 12), selectmode=tk.SINGLE, height=5)
        self.lista_resultado.grid(row=3, column=1, pady=10)
        
        # boton de crear competencia
        self.btn_crear_competencia = tk.Button(
            self, 
            text='Crear competencia', 
            font=('Arial', 12), 
            width=14, 
            bg='green', 
            fg="white",
            command=self.agregar_competencia
        )
        self.btn_crear_competencia.grid(row=4, column=0, columnspan=1, pady=20)
        
        # Boton de editar competencia
        self.btn_editar_competencia = tk.Button(
            self, 
            text='Editar competencia', 
            font=('Arial', 12), 
            width=14, 
            bg='blue', 
            fg="white"
        )
        self.btn_editar_competencia.grid(row=4, column=1, columnspan=1, pady=20)
        
        # Boton de eliminar competencia
        self.btn_eliminar_competencia = tk.Button(
            self, 
            text='Eliminar competencia', 
            font=('Arial', 12), 
            width=14, 
            bg='red', 
            fg="white"
        )
        self.btn_eliminar_competencia.grid(row=4, column=2, columnspan=1, pady=20)
        
        #Labels para mostrar tipo lista para todas las competencias
        
        
        # Conectar a la base de datos y recuperar los nombres de los programas
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_programa FROM programa")
        programas = cursor.fetchall()
        conexion.close()
        for programa in programas:
            self.lista_programa.insert(tk.END, programa[0])
        
        # Conectar a la base de datos y recuperar los nombres de los resultados de aprendizaje
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT resultado_aprendizaje FROM resultado_aprendizaje")
        resultados = cursor.fetchall()
        conexion.close()
        for resultado in resultados:
            self.lista_resultado.insert(tk.END, resultado[0])
            
        
    # # Metodo para mostrar el listado de las competencias
    # def listar_competencias(self):
    #     conexion = sqlite3.connect('sistema_sena.db')
    #     cursor = conexion.cursor()
    #     cursor.execute("SELECT * FROM competencia")
    #     competencias = cursor.fetchall()
    #     conexion.close()
        
    #     for i, competencia in enumerate(competencias, start=1):
    #         lbl_competencia = tk.Label(
    #             self.container_labels_competencias,
    #             text=f"Competencia {i}: {competencia[1]} - Programa: {competencia[2]} - Resultado: {competencia[3]}",
    #             font=('Arial', 12)
    #         )
    #         lbl_competencia.pack(pady=5)
            
    # Metodo para agregar una competencia
    def agregar_competencia(self):
        try:
            nueva_competencia = self.txt_nombre_competencia.get().strip()
            nueva_competencia_programa = self.lista_programa.get(tk.ACTIVE)
            nueva_competencia_resultado = self.lista_resultado.get(tk.ACTIVE)
            if nueva_competencia and nueva_competencia_programa and nueva_competencia_resultado:
                conexion = sqlite3.connect('sistema_sena.db')
                cursor = conexion.cursor()
                cursor.execute("INSERT INTO competencia (nombre_competencia, id_programa, id_resultado_aprendizaje) VALUES (?, ?, ?)", (nueva_competencia, nueva_competencia_programa, nueva_competencia_resultado,))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Creado con éxito.", "Nueva competencia agregada con éxito.")
        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error al crear el nuevo registro: {error}")

programa = CRUDCompetencia()
programa.mainloop()
