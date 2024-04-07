import tkinter as tk
from tkinter import messagebox
import sqlite3

class CRUDCompetencia(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        # Dimensiones y titulo de la ventana
        self.geometry("800x800")
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
            text='Crear', 
            font=('Arial', 12), 
            width=10, 
            bg='green', 
            fg="white",
            command=self.agregar_competencia
        )
        self.btn_crear_competencia.grid(row=4, column=0, columnspan=1, pady=20)
        
        # Boton de editar competencia
        self.btn_editar_competencia = tk.Button(
            self, 
            text='Editar', 
            font=('Arial', 12), 
            width=10, 
            bg='blue', 
            fg="white",
            command=self.editar_competencia
        )
        self.btn_editar_competencia.grid(row=4, column=1, columnspan=1, pady=20)
        
        # Boton de eliminar competencia
        self.btn_eliminar_competencia = tk.Button(
            self, 
            text='Eliminar', 
            font=('Arial', 12), 
            width=10, 
            bg='red', 
            fg="white",
            command=self.eliminar_competencia
        )
        self.btn_eliminar_competencia.grid(row=4, column=2, columnspan=1, pady=20)
        
        #Labels para mostrar tipo lista para todas las competencias
        # TITULO ID COMPETENCIA
        self.titulo_id_competencia = tk.Label(self, text='ID', font=('Arial', 15, 'bold'))
        self.titulo_id_competencia.grid(row=5, column=0, pady=10)
        
        # TITULO NOMBRE DE COMPETENCIA
        self.titulo_nombre_competencia = tk.Label(self, text='Nombre de \ncompetencia', font=('Arial', 15, 'bold'))
        self.titulo_nombre_competencia.grid(row=5, column=1, pady=10)
        
        # TITULO PROGRAMA
        self.titulo_programa = tk.Label(self, text='Programa', font=('Arial', 15, 'bold'))
        self.titulo_programa.grid(row=5, column=2, pady=10)
        
        # TITULO RESULTADO
        self.titulo_resultado = tk.Label(self, text='Resultado', font=('Arial', 15, 'bold'))
        self.titulo_resultado.grid(row=5, column=3, pady=10)
        
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
            
        # Mostrar los registros
        self.mostrar_registros()
    
    # Metodo para mostrar el listado de las competencias
    def mostrar_registros(self):
        # for widget in self.winfo_children():
        #     widget.grid_forget()
        
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM competencia")
        competencias = cursor.fetchall()
        conexion.close()
        
        for i, competencia in enumerate(competencias, start=1):
            # MOSTRAR REGISTROS ID COMPETENCIA
            self.mostrar_id_competencia = tk.Label(self, text=competencia[0], font=('Arial', 12))
            self.mostrar_id_competencia.grid(row=i+5, column=0, pady=10)
        
            # MOSTRAR REGISTROS NOMBRE COMPETENCIA
            self.mostrar_nombre_competencia = tk.Label(self, text=competencia[1], font=('Arial', 12))
            self.mostrar_nombre_competencia.grid(row=i+5, column=1, pady=10)
            
            # MOSTRAR REGISTROS PROGRAMA
            self.mostrar_programa = tk.Label(self, text=competencia[2], font=('Arial', 12))
            self.mostrar_programa.grid(row=i+5, column=2, pady=10)
        
            # MOSTRAR REGISTROS RESULTADO DE APTRENDIZAJE
            self.mostrar_reusltado = tk.Label(self, text=competencia[3], font=('Arial', 12))
            self.mostrar_reusltado.grid(row=i+5, column=3, pady=10)
            
            # MOSTRAR BOTON PARA ACCION
            self.btn_accion = tk.Button(self, 
            text='Seleccionar', 
            font=('Arial', 12), 
            width=10, 
            bg='blue', 
            fg="white",
            command= lambda c=competencia: self.mostrar_registro_a_eliminar_y_editar(c)
            )
            self.btn_accion.grid(row=i+5, column=4, columnspan=1, pady=10)

    # Metodo para seleccionar un registro a editar o eliminar
    def mostrar_registro_a_eliminar_y_editar(self, competencia):
        self.txt_nombre_competencia.delete(0, tk.END)
        self.txt_nombre_competencia.insert(0, competencia[1])
        
        self.lista_programa.insert(tk.END)
        
        self.lista_resultado.insert(tk.END)
        
        self.registro_seleccionado = competencia
    
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
                # Mostrar los registros
                self.mostrar_registros()
        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error al crear el nuevo registro: {error}")
    
    # Metodo para eliminar un registro
    def eliminar_competencia(self):
        try:
            if hasattr(self, 'registro_seleccionado'):
                competencia = self.registro_seleccionado
                conexion = sqlite3.connect('sistema_sena.db')
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM competencia WHERE id_competencia = ?", (competencia[0],))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Eliminado con éxito.", "Competencia eliminada con éxito.")
                # Mostrar los registros
                self.mostrar_registros()
            else:
                messagebox.showwarning("Advertencia", "Primero selecciona una competencia.")
        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error al eliminar el registro: {error}")
    
    # Método para editar una competencia
    def editar_competencia(self):
        try:
            if hasattr(self, 'registro_seleccionado'):
                competencia = self.registro_seleccionado
                nueva_competencia_nombre = self.txt_nombre_competencia.get().strip()
                nuevo_programa = self.lista_programa.get(tk.ACTIVE)
                nuevo_resultado = self.lista_resultado.get(tk.ACTIVE)

                if nueva_competencia_nombre and nuevo_programa and nuevo_resultado:
                    conexion = sqlite3.connect('sistema_sena.db')
                    cursor = conexion.cursor()
                    cursor.execute("UPDATE competencia SET nombre_competencia= ?, id_programa= ?, id_resultado_aprendizaje= ? WHERE id_competencia = ?", (nueva_competencia_nombre, nuevo_programa, nuevo_resultado, competencia[0]))
                    conexion.commit()
                    conexion.close()
                    messagebox.showinfo("Actualizado con éxito.", "Competencia actualizada con éxito.")
                    # Mostrar los registros
                    self.mostrar_registros()
                else:
                    messagebox.showwarning("Advertencia", "Por favor complete todos los campos.")
            else:
                messagebox.showwarning("Advertencia", "Primero selecciona una competencia.")
        except sqlite3.Error as error:
            messagebox.showerror("Error", f"Error al actualizar el registro: {error}")
