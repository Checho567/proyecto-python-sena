import tkinter as tk
from tkinter import messagebox
import sqlite3
import datetime

class CRUDActividad(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        #Cosas generales de la ventana
        self.geometry("1450x700")
        self.title("Sistema Sena")
        
        #Titulo de la ventana
        self.titulo = tk.Label(self, text='Panel de actividades', font=('Arial', 22))
        self.titulo.grid(row=0, column=2, pady=2)
        
        # Inicio labels para los campos
        self.lbl_desc_actividad = tk.Label(
            self, 
            text='Descripción \nactividad', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_desc_actividad.grid(row=1, column=0, padx=50, pady=10)
        
        self.lbl_fecha_asignacion = tk.Label(
            self, 
            text='Fecha de \nasignación', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_fecha_asignacion.grid(row=1, column=1, pady=10)
        
        self.lbl_fecha_entrega = tk.Label(
            self, 
            text='Fecha de \nentrega', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_fecha_entrega.grid(row=1, column=2, pady=10, padx=80)
        
        self.lbl_tipo_actividad = tk.Label(
            self, 
            text='Tipo de \nactividad', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_tipo_actividad.grid(row=1, column=3, pady=10)
        
        self.lbl_nota = tk.Label(
            self, 
            text='Nota', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_nota.grid(row=1, column=4, pady=10, padx=80)
        
        self.lbl_instructor = tk.Label(
            self, 
            text='Instructor', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_instructor.grid(row=1, column=5, pady=10)
        # Fin labels para los campos
        
        #Inicio inputs de los campos
        self.txt_desc_actividad = tk.Entry(self, width=15, font=('Arial', 12))
        self.txt_desc_actividad.grid(row=2, column=0, pady=5)
        
        self.aviso_fecha_asig = tk.Label(
            self, 
            text='*La fecha se pone \nautomáticamente*', 
            font=('Arial', 12, 'bold'),
            fg='black'
        )
        self.aviso_fecha_asig.grid(row=2, column=1, pady=5)
        
        self.txt_fecha_entrega = tk.Entry(self, width=15, font=('Arial', 12))
        self.txt_fecha_entrega.grid(row=2, column=2, pady=5)
        
        self.lista_tipo_actividad = tk.Listbox(self, font=('Arial', 12), selectmode=tk.SINGLE, height=5)
        self.lista_tipo_actividad.grid(row=2, column=3, pady=5)
        
        self.lista_nota = tk.Listbox(self, font=('Arial', 12), selectmode=tk.SINGLE, height=5, width=8)
        self.lista_nota.grid(row=2, column=4, pady=5)
        
        self.lista_instructor = tk.Listbox(self, font=('Arial', 12), selectmode=tk.SINGLE, height=5)
        self.lista_instructor.grid(row=2, column=5, pady=5)
        #Fin inputs de los campos
        
        #Inicio botones para acciones
        #boton de crear actividad
        self.btn_crear_actividad = tk.Button(
            self,
            text='Crear', 
            font=('Arial', 15), 
            width=15, 
            bg='green', 
            fg="white",
            command=self.agregar_actividad
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
            command=self.editar_actividad
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
            command=self.eliminar_actividad
        )
        self.btn_eliminar_actividad.grid(row=3, column=5, pady=20)
        #Fin botones para acciones
        
        # Inicio labels para mostrar los campos
        self.mostrar_desc_actividad = tk.Label(
            self, 
            text='Descripción \nactividad', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_desc_actividad.grid(row=4, column=0, padx=50, pady=10)
        
        self.mostrar_fecha_asignacion = tk.Label(
            self, 
            text='Fecha de \nasignación', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_fecha_asignacion.grid(row=4, column=1, pady=10, padx=50)
        
        self.mostrar_fecha_entrega = tk.Label(
            self, 
            text='Fecha de \nentrega', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_fecha_entrega.grid(row=4, column=2, pady=10, padx=80)
        
        self.mostrar_tipo_actividad = tk.Label(
            self, 
            text='Tipo de \nactividad', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_tipo_actividad.grid(row=4, column=3, pady=10)
        
        self.mostrar_nota = tk.Label(
            self, 
            text='Nota', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_nota.grid(row=4, column=4, pady=10, padx=80)
        
        self.mostrar_instructor = tk.Label(
            self, 
            text='Instructor', 
            font=('Arial', 15, 'bold'),
            fg='black'
        )
        self.mostrar_instructor.grid(row=4, column=5, pady=10)
        # Fin labels para mostrar los campos
        
        # Recuperar los nombres de los tipos de actividad
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT tipo_actividad FROM tipo_actividad")
        tipos = cursor.fetchall()
        conexion.close()
        for tipo in tipos:
            self.lista_tipo_actividad.insert(tk.END, tipo[0])
            
        # Recuperar los numeros de las notas
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT nota FROM nota")
        notas = cursor.fetchall()
        conexion.close()
        for nota in notas:
            self.lista_nota.insert(tk.END, nota[0])
            
        # Recuperar los nombres de los instructores
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre_instructor FROM instructor")
        instructores = cursor.fetchall()
        conexion.close()
        for instructor in instructores:
            self.lista_instructor.insert(tk.END, instructor[0])
        
        self.mostrar_registros()
    
    # Metodo para mostrar registros
    def mostrar_registros(self):
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM actividad")
        actividades = cursor.fetchall()
        conexion.close()
        
        for i, actividad in enumerate(actividades, start=1):
            self.mostrar_datos_desc_actividad = tk.Label(self, text=actividad[1], font=('Arial', 12))
            self.mostrar_datos_desc_actividad.grid(row=i+5, column=0, padx=50, pady=10)
            
            self.mostrar_datos_fecha_asignacion = tk.Label(self, text=actividad[2], font=('Arial', 12))
            self.mostrar_datos_fecha_asignacion.grid(row=i+5, column=1, padx=50, pady=10)
            
            self.mostrar_datos_fecha_entrega = tk.Label(self, text=actividad[3], font=('Arial', 12))
            self.mostrar_datos_fecha_entrega.grid(row=i+5, column=2, padx=50, pady=10)
            
            self.mostrar_datos_tipo_actividad = tk.Label(self, text=actividad[4], font=('Arial', 12))
            self.mostrar_datos_tipo_actividad.grid(row=i+5, column=3, padx=50, pady=10)
            
            self.mostrar_datos_nota = tk.Label(self, text=actividad[5], font=('Arial', 12))
            self.mostrar_datos_nota.grid(row=i+5, column=4, padx=50, pady=10)
            
            self.mostrar_datos_instructor = tk.Label(self, text=actividad[6], font=('Arial', 12))
            self.mostrar_datos_instructor.grid(row=i+5, column=5, padx=50, pady=10)
            
            self.btn_accion = tk.Button(self, 
            text='Seleccionar', 
            font=('Arial', 12), 
            width=10, 
            bg='blue', 
            fg="white",
            command= lambda c=actividad: self.mostrar_registro_a_eliminar_y_editar(c)
            )
            self.btn_accion.grid(row=i+5, column=6, columnspan=1, pady=10)
    
    # Metodo para seleccionar un registro a editar o eliminar
    def mostrar_registro_a_eliminar_y_editar(self, actividad):
        self.txt_desc_actividad.delete(0, tk.END)
        self.txt_desc_actividad.insert(0, actividad[1])
        
        self.txt_fecha_entrega.delete(0, tk.END)
        self.txt_fecha_entrega.insert(0, actividad[3])
        
        self.lista_tipo_actividad.insert(tk.END)
        self.lista_nota.insert(tk.END)
        self.lista_instructor.insert(tk.END)
        
        self.registro_seleccionado = actividad
    
    # Metodo para crear registros de actividades
    def agregar_actividad(self):
        try:
            nv_desc_act = self.txt_desc_actividad.get().strip()
            nv_fecha_asignacion = datetime.date.today()
            nv_fecha_entrega = self.txt_fecha_entrega.get()
            nv_tipo_act = self.lista_tipo_actividad.get(tk.ACTIVE)
            nv_nota = self.lista_nota.get(tk.ACTIVE)
            nv_instructor = self.lista_instructor.get(tk.ACTIVE)
            if nv_desc_act and nv_fecha_asignacion and nv_fecha_entrega and nv_tipo_act and nv_nota and nv_instructor:
                conexion = sqlite3.connect('sistema_sena.db')
                cursor = conexion.cursor()
                cursor.execute('''INSERT INTO actividad (
                    descripcion_actividad, 
                    fecha_asignacion, 
                    fecha_entrega,
                    id_tipo_actividad,
                    id_nota,
                    id_instructor) VALUES (?, ?, ?, ?, ?, ?)''',
                    (nv_desc_act, nv_fecha_asignacion, nv_fecha_entrega, nv_tipo_act, nv_nota, nv_instructor))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Nueva actividad registrada con exito")
                self.mostrar_registros()
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
    
    #Metodo para eliminar un registro
    def eliminar_actividad(self):
        try:
            if hasattr(self, 'registro_seleccionado'):
                actividad = self.registro_seleccionado
                conexion = sqlite3.connect('sistema_sena.db')
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM actividad WHERE id_actividad = ?", (actividad[0],))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Eliminado con éxito.", "Actividad eliminada con éxito.")
                self.mostrar_registros()
            else:
                messagebox.showwarning("Advertencia", "Primero selecciona una actividad.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
    
    def editar_actividad(self):
        try:
            if hasattr(self, 'registro_seleccionado'):
                actividad = self.registro_seleccionado
                edit_desc_actividad = self.txt_desc_actividad.get().strip()
                edit_fecha_entrega = self.txt_fecha_entrega.get()
                edit_tipo_actividad = self.lista_tipo_actividad.get(tk.ACTIVE)
                edit_nota = self.lista_nota.get(tk.ACTIVE)
                edit_instructor = self.lista_instructor.get(tk.ACTIVE)
                if edit_desc_actividad and edit_fecha_entrega and edit_tipo_actividad and edit_nota and edit_instructor:
                    conexion = sqlite3.connect('sistema_sena.db')
                    cursor = conexion.cursor()
                    cursor.execute('''UPDATE actividad SET 
                                descripcion_actividad = ?, 
                                fecha_entrega = ?, 
                                id_tipo_actividad = ?,
                                id_nota = ?,
                                id_instructor = ? 
                                WHERE id_actividad = ?''', (
                                    edit_desc_actividad, 
                                    edit_fecha_entrega, 
                                    edit_tipo_actividad,
                                    edit_nota,
                                    edit_instructor,
                                    actividad[0]))
                    conexion.commit()
                    conexion.close()
                    messagebox.showinfo("Actualizado con éxito.", "Competencia actualizada con éxito.")
                    # Mostrar los registros
                    self.mostrar_registros()
                else:
                    messagebox.showwarning("Advertencia", "Por favor completa todos los campos.")
            else:
                messagebox.showwarning("Advertencia", "Primero selecciona una competencia.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")