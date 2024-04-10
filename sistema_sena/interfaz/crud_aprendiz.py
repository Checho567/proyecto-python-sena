import tkinter as tk
from tkinter import messagebox
import sqlite3

class CRUDAprendiz(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.attributes("-fullscreen", True)
        self.title("Sistema Sena")
        
        #Titulo de la ventana
        self.titulo = tk.Label(self, text='Panel de Aprendices', font=('Arial', 22))
        self.titulo.grid(row=0, column=2, pady=15)
        
        # Inicio de labels para los inputs
        self.lbl_nombre_aprendiz = tk.Label(
            self, 
            text='Nombre de \naprendiz', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_nombre_aprendiz.grid(row=1, column=0, pady=10)
        
        self.lbl_ficha = tk.Label(
            self, 
            text='Número de \nficha', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_ficha.grid(row=1, column=1, pady=10)
        
        self.lbl_jornada = tk.Label(
            self, 
            text='Jornada', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_jornada.grid(row=1, column=2, pady=10)
        
        self.lbl_programa = tk.Label(
            self, 
            text='Programa', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_programa.grid(row=1, column=3, pady=10)
        
        self.lbl_instructor = tk.Label(
            self, 
            text='Instructor', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_instructor.grid(row=1, column=4, pady=10)
        
        self.lbl_actividad = tk.Label(
            self, 
            text='Actividad', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_actividad.grid(row=1, column=5, pady=10, padx=80)
        
        self.lbl_resultado_aprendizaje = tk.Label(
            self, 
            text='Resultado de \naprendizaje', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_resultado_aprendizaje.grid(row=1, column=6, pady=10, padx=80)
        # Fin de labels para los inputs
        
        # Inicio inputs para los campos
        self.txt_nombre_aprendiz = tk.Entry(self, width=15, font=('Arial', 12))
        self.txt_nombre_aprendiz.grid(row=2, column=0, pady=5)
        
        self.txt_ficha = tk.Entry(self, width=12, font=('Arial', 12))
        self.txt_ficha.grid(row=2, column=1, pady=5)
        
        self.txt_jornada = tk.Entry(self, width=12, font=('Arial', 12))
        self.txt_jornada.grid(row=2, column=2, pady=5)
        
        self.lista_programa = tk.Listbox(self, font=('Arial', 12), selectmode=tk.SINGLE, height=5)
        self.lista_programa.grid(row=2, column=3, pady=5)
        
        self.lista_instructor = tk.Listbox(self, font=('Arial', 12), selectmode=tk.SINGLE, height=5)
        self.lista_instructor.grid(row=2, column=4, pady=5, padx=80)
        
        self.lista_actividad = tk.Listbox(self, font=('Arial', 12), selectmode=tk.SINGLE, height=5)
        self.lista_actividad.grid(row=2, column=5, pady=5)
        
        self.lista_resultado = tk.Listbox(self, font=('Arial', 12), selectmode=tk.SINGLE, height=5)
        self.lista_resultado.grid(row=2, column=6, pady=5)
        # Fin inputs para los campos
        
        #Inicio botones para acciones
        #boton de crear actividad
        self.btn_crear_actividad = tk.Button(
            self,
            text='Crear', 
            font=('Arial', 15), 
            width=15, 
            bg='green', 
            fg="white",
            command=self.crear_estudiante
        )
        self.btn_crear_actividad.grid(row=3, column=1, pady=20)
        
        #boton de editar actividad
        self.btn_editar_actividad = tk.Button(
            self,
            text='Editar', 
            font=('Arial', 15), 
            width=15, 
            bg='blue', 
            fg="white",
            command=self.editar_estudiante
        )
        self.btn_editar_actividad.grid(row=3, column=3, pady=20)
        
        #boton de eliminar_actividad
        self.btn_eliminar_actividad = tk.Button(
            self,
            text='Eliminar', 
            font=('Arial', 15), 
            width=15, 
            bg='red', 
            fg="white",
            command=self.eliminar_estudiante
        )
        self.btn_eliminar_actividad.grid(row=3, column=5, pady=20)
        #Fin botones para acciones
        
        # Inicio labels tipo tabla para los registros
        self.mostrar_nombre_aprendiz = tk.Label(
            self, 
            text='Nombre del \naprendiz', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_nombre_aprendiz.grid(row=4, column=0, pady=10)
        
        self.mostrar_ficha = tk.Label(
            self, 
            text='Número de \nficha', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_ficha.grid(row=4, column=1, pady=10)
        
        self.mostrar_jornada = tk.Label(
            self, 
            text='Jornada', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_jornada.grid(row=4, column=2, pady=10)
        
        self.mostrar_programa = tk.Label(
            self, 
            text='Programa', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_programa.grid(row=4, column=3, pady=10)
        
        self.mostrar_instructor = tk.Label(
            self, 
            text='Instructor', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_instructor.grid(row=4, column=4, pady=10)
        
        self.mostrar_actividad = tk.Label(
            self, 
            text='Actividad', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_actividad.grid(row=4, column=5, pady=10)
        
        self.mostrar_resultado = tk.Label(
            self, 
            text='Resultado de \naprendizaje', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_resultado.grid(row=4, column=6, pady=10)
        # Fin labels tipo tabla para los registros
        
        # Recuperar los nombres de los programas
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_programa FROM programa")
        programas = cursor.fetchall()
        conexion.close()
        for programa in programas:
            self.lista_programa.insert(tk.END, programa[0])
            
        # Recuperar los nombres de los instructores
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_instructor FROM instructor")
        instructores = cursor.fetchall()
        conexion.close()
        for instructor in instructores:
            self.lista_instructor.insert(tk.END, instructor[0])
        
        # Recuperar las descripciones de las actividades
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT descripcion_actividad FROM actividad")
        actividades = cursor.fetchall()
        conexion.close()
        for actividad in actividades:
            self.lista_actividad.insert(tk.END, actividad[0])
        
        # Recuperar las descripciones de las actividades
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT resultado_aprendizaje FROM resultado_aprendizaje")
        resultados = cursor.fetchall()
        conexion.close()
        for resultado in resultados:
            self.lista_resultado.insert(tk.END, resultado[0])
            
        # Mostrar los registros
        self.mostrar_registros()
        
    # Metodo para listar los registros
    def mostrar_registros(self):
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM aprendiz")
        aprendices = cursor.fetchall()
        conexion.close()
        
        for i, aprendiz in enumerate(aprendices, start=1):
            self.mostrar_datos_nombre = tk.Label(self, text=aprendiz[1], font=('Arial', 12))
            self.mostrar_datos_nombre.grid(row=i+5, column=0, pady=10)
            
            self.mostrar_datos_ficha = tk.Label(self, text=aprendiz[2], font=('Arial', 12))
            self.mostrar_datos_ficha.grid(row=i+5, column=1, pady=10)
            
            self.mostrar_datos_jornada = tk.Label(self, text=aprendiz[3], font=('Arial', 12))
            self.mostrar_datos_jornada.grid(row=i+5, column=2, pady=10)
            
            self.mostrar_datos_programa = tk.Label(self, text=aprendiz[4], font=('Arial', 12))
            self.mostrar_datos_programa.grid(row=i+5, column=3, pady=10)
            
            self.mostrar_datos_instructor = tk.Label(self, text=aprendiz[6], font=('Arial', 12))
            self.mostrar_datos_instructor.grid(row=i+5, column=4, pady=10)
            
            self.mostrar_datos_actividad = tk.Label(self, text=aprendiz[7], font=('Arial', 12))
            self.mostrar_datos_actividad.grid(row=i+5, column=5, pady=10)
            
            self.mostrar_resultado = tk.Label(self, text=aprendiz[5], font=('Arial', 12))
            self.mostrar_resultado.grid(row=i+5, column=6, pady=10)
            
            self.btn_accion = tk.Button(self, 
            text='Seleccionar', 
            font=('Arial', 12), 
            width=10, 
            bg='blue', 
            fg="white",
            command= lambda c=aprendiz: self.mostrar_registro_a_eliminar_y_editar(c)
            )
            self.btn_accion.grid(row=i+5, column=7, columnspan=1, pady=10)
    
    # Metodo para seleccionar un registro a editar o eliminar
    def mostrar_registro_a_eliminar_y_editar(self, aprendiz):
        self.txt_nombre_aprendiz.delete(0, tk.END)
        self.txt_nombre_aprendiz.insert(0, aprendiz[1])
        
        self.txt_ficha.delete(0, tk.END)
        self.txt_ficha.insert(0, aprendiz[2])
        
        self.txt_jornada.delete(0, tk.END)
        self.txt_jornada.insert(0, aprendiz[3])
        
        self.lista_programa.insert(tk.END)
        self.lista_instructor.insert(tk.END)
        self.lista_actividad.insert(tk.END)
        self.lista_resultado.insert(tk.END)
        
        self.registro_seleccionado = aprendiz
    
    #Metodo para crear nuevo estudiante
    def crear_estudiante(self):
        try:
            nv_nombre_aprendiz = self.txt_nombre_aprendiz.get().strip()
            nv_ficha = self.txt_ficha.get()
            nv_jornada = self.txt_jornada.get()
            nv_programa = self.lista_programa.get(tk.ACTIVE)
            nv_instructor = self.lista_instructor.get(tk.ACTIVE)
            nv_actividad = self.lista_actividad.get(tk.ACTIVE)
            nv_resultado = self.lista_resultado.get(tk.ACTIVE)
            if nv_nombre_aprendiz and nv_ficha and nv_jornada and nv_programa and nv_instructor and nv_resultado:
                conexion = sqlite3.connect('sistema_sena.db')
                cursor = conexion.cursor()
                cursor.execute('''INSERT INTO aprendiz (
                    nombre, 
                    ficha, 
                    jornada,
                    id_programa,
                    id_instructor,
                    id_actividad,
                    id_resultado_aprendizaje) VALUES (?, ?, ?, ?, ?, ?, ?)''',(
                        nv_nombre_aprendiz, 
                        nv_ficha,
                        nv_jornada, 
                        nv_programa,
                        nv_instructor,
                        nv_actividad,
                        nv_resultado
                        )
                    )
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Nuevo aprendiz registrado con exito")
                # Mostrar los registros
                self.mostrar_registros()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
            
    # Metodo para eliminar a un estudiante
    def eliminar_estudiante(self):
        try:
            if hasattr(self, 'registro_seleccionado'):
                aprendiz = self.registro_seleccionado
                conexion = sqlite3.connect('sistema_sena.db')
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM aprendiz WHERE id_aprendiz = ?", (aprendiz[0],))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Eliminado con éxito.", "Aprendiz eliminado con éxito.")
                # Mostrar los registros
                self.mostrar_registros()
            else:
                messagebox.showwarning("Advertencia", "Primero selecciona a un aprendiz.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
    
    #Metodo para editar un registro de aprendices
    def editar_estudiante(self):
        try:
            if hasattr(self, 'registro_seleccionado'):
                aprendiz = self.registro_seleccionado
                edit_nombre_aprendiz = self.txt_nombre_aprendiz.get().strip()
                edit_ficha = self.txt_ficha.get()
                edit_jornada = self.txt_jornada.get()
                edit_programa = self.lista_programa.get(tk.ACTIVE)
                edit_instructor = self.lista_instructor.get(tk.ACTIVE)
                edit_actividad = self.lista_actividad.get(tk.ACTIVE)
                edit_resultado = self.lista_resultado.get(tk.ACTIVE)
                if edit_nombre_aprendiz and edit_ficha and edit_jornada and edit_programa and edit_instructor and edit_resultado:
                    conexion = sqlite3.connect('sistema_sena.db')
                    cursor = conexion.cursor()
                    cursor.execute('''UPDATE aprendiz SET
                                    nombre = ?,
                                    ficha = ?,
                                    jornada = ?,
                                    id_programa = ?,
                                    id_instructor = ?,
                                    id_actividad = ?,
                                    id_resultado_aprendizaje = ?
                                    WHERE id_aprendiz = ?''', (
                                    edit_nombre_aprendiz, 
                                    edit_ficha,
                                    edit_jornada,
                                    edit_programa,
                                    edit_instructor,
                                    edit_actividad,
                                    edit_resultado,
                                    aprendiz[0]
                                    ))
                    conexion.commit()
                    conexion.close()
                    messagebox.showinfo("Actualizado con éxito.", "Aprendiz actualizado con éxito.")
                    # Mostrar los registros
                    self.mostrar_registros()
                else:
                    messagebox.showwarning("Advertencia", "Por favor completa todos los campos.")
            else:
                messagebox.showwarning("Advertencia", "Primero selecciona a un aprendiz.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

aprendiz = CRUDAprendiz()
aprendiz.mainloop()