import tkinter as tk
from tkinter import messagebox
import sqlite3

class CRUDNota(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry("1050x500")
        self.title("Sistema Sena")
        
        #Titulo de la ventana
        self.titulo = tk.Label(self, text='Panel de Notas', font=('Arial', 22))
        self.titulo.grid(row=0, column=2, pady=2)
        
        # Inicio labels para los campos
        self.lbl_aprendiz = tk.Label(
            self, 
            text='Aprendiz', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_aprendiz.grid(row=1, column=0, pady=10, padx=100)
        
        self.lbl_nota_1 = tk.Label(
            self, 
            text='Nota 1', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_nota_1.grid(row=1, column=1, pady=10)
        
        self.lbl_nota_2 = tk.Label(
            self, 
            text='Nota 2', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_nota_2.grid(row=1, column=2, pady=10)
        
        self.lbl_nota_3 = tk.Label(
            self, 
            text='Nota 3', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.lbl_nota_3.grid(row=1, column=3, pady=10)
        # Fin labels para los campos
        
        #Inicio inputs de los campos
        self.lista_aprendiz = tk.Listbox(self, font=('Arial', 12), selectmode=tk.SINGLE, height=5)
        self.lista_aprendiz.grid(row=2, column=0, pady=5)
        
        self.txt_nota_1 = tk.Entry(self, width=5, font=('Arial', 12))
        self.txt_nota_1.grid(row=2, column=1, pady=5)
        
        self.txt_nota_2 = tk.Entry(self, width=5, font=('Arial', 12))
        self.txt_nota_2.grid(row=2, column=2, pady=5)
        
        self.txt_nota_3 = tk.Entry(self, width=5, font=('Arial', 12))
        self.txt_nota_3.grid(row=2, column=3, pady=5)
        #Fin inputs de los campos
        
        #Inicio botones para acciones
        #boton de crear actividad
        self.btn_crear_nota = tk.Button(
            self,
            text='Crear', 
            font=('Arial', 12), 
            width=15, 
            bg='green', 
            fg="white",
            command=self.crear_nota
        )
        self.btn_crear_nota.grid(row=3, column=0, pady=20)
        
        #boton de editar actividad
        self.btn_editar_nota = tk.Button(
            self,
            text='Editar', 
            font=('Arial', 12), 
            width=12, 
            bg='blue', 
            fg="white",
            command=self.editar_nota
        )
        self.btn_editar_nota.grid(row=3, column=1, pady=20)
        
        #boton de eliminar_actividad
        self.btn_eliminar_nota = tk.Button(
            self,
            text='Eliminar', 
            font=('Arial', 12), 
            width=12, 
            bg='red', 
            fg="white",
            command=self.eliminar_nota
        )
        self.btn_eliminar_nota.grid(row=3, column=2, pady=20)
        #Fin botones para acciones
        
        # Inicio labels para mostrar los campos
        self.mostrar_aprendiz = tk.Label(
            self, 
            text='Aprendiz', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.mostrar_aprendiz.grid(row=4, column=0, pady=10)
        
        self.mostrar_nota_1 = tk.Label(
            self, 
            text='Nota 1', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.mostrar_nota_1.grid(row=4, column=1, pady=10)
        
        self.mostrar_nota_2 = tk.Label(
            self,
            text='Nota 2', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.mostrar_nota_2.grid(row=4, column=2, pady=10)
        
        self.mostrar_nota_3 = tk.Label(
            self, 
            text='Nota 3', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.mostrar_nota_3.grid(row=4, column=3, pady=10)
        
        self.mostrar_promedio = tk.Label(
            self, 
            text='Promedio', 
            font=('Arial', 15, 'bold'), 
            bg='green',
            fg='white'
        )
        self.mostrar_promedio.grid(row=4, column=4, pady=10, padx=50)
        # Fin labels para mostrar los campos
        
        # Recuperar nombres para mostrar aprendices
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre FROM aprendiz")
        aprendices = cursor.fetchall()
        conexion.close()
        for aprendiz in aprendices:
            self.lista_aprendiz.insert(tk.END, aprendiz[0])
        
        #Mostrar los datos de las notas
        self.mostrar_notas()
        
    # Metodo para mostrar las notas por aprendiz
    def mostrar_notas(self):
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM nota")
        notas = cursor.fetchall()
        conexion.close()
        for i, nota in enumerate(notas, start=1):
            self.mostrar_datos_aprendiz = tk.Label(self, text=nota[5], font=('Arial', 12))
            self.mostrar_datos_aprendiz.grid(row=i+5, column=0, pady=10)
            
            self.mostrar_datos_nota_1 = tk.Label(self, text=nota[1], font=('Arial', 12))
            self.mostrar_datos_nota_1 .grid(row=i+5, column=1, pady=10)
            
            self.mostrar_datos_nota_2 = tk.Label(self, text=nota[2], font=('Arial', 12))
            self.mostrar_datos_nota_2 .grid(row=i+5, column=2, pady=10)
            
            self.mostrar_datos_nota_3 = tk.Label(self, text=nota[3], font=('Arial', 12))
            self.mostrar_datos_nota_3 .grid(row=i+5, column=3, pady=10)
            
            self.mostrar_datos_promedio = tk.Label(self, text=nota[4], font=('Arial', 12))
            self.mostrar_datos_promedio .grid(row=i+5, column=4, pady=10)
            
            self.btn_accion = tk.Button(self, 
            text='Seleccionar', 
            font=('Arial', 12), 
            width=10, 
            bg='blue', 
            fg="white",
            command= lambda c=nota: self.mostrar_registro_a_eliminar_y_editar(c)
            )
            self.btn_accion.grid(row=i+5, column=5, columnspan=1, pady=10)
            
    # Metodo para seleccionar un registro a editar o eliminar
    def mostrar_registro_a_eliminar_y_editar(self, nota):
        self.lista_aprendiz.insert(tk.END)
        self.txt_nota_1.insert(0, nota[1])
        self.txt_nota_2.insert(0, nota[2])
        self.txt_nota_3.insert(0, nota[3])
        self.registro_seleccionado = nota
        
    def eliminar_nota(self):
        try:
            if hasattr(self, 'registro_seleccionado'):
                nota = self.registro_seleccionado
                conexion = sqlite3.connect('sistema_sena.db')
                cursor = conexion.cursor()
                cursor.execute('''DELETE FROM nota WHERE id_nota = ?''', (nota[0],))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Eliminado con éxito.", "Nota eliminada con éxito.")
                
                #Mostrar registros y limpiar cajas
                self.limpiar_cajas()
                self.mostrar_notas()
            else:
                messagebox.showwarning("Advertencia", "Primero selecciona una nota.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
    
    #Metodo para crear una nota para un aprendiz
    def crear_nota(self):
        nv_aprendiz = self.lista_aprendiz.get(tk.ACTIVE)
        nv_nota_1 = int(self.txt_nota_1.get())
        nv_nota_2 = int(self.txt_nota_2.get())
        nv_nota_3 = int(self.txt_nota_3.get())
        nv_promedio = int((nv_nota_1 + nv_nota_2 + nv_nota_3) / 3)
        
        if nv_nota_1 > 100 or nv_nota_2 > 100 or nv_nota_3 > 100:
            messagebox.showwarning("Advertencia", f"Debes añadir una nota igual o menor a 100")
        else:
            if nv_aprendiz and nv_nota_1 and nv_nota_2 and nv_nota_3 and nv_promedio:
                conexion = sqlite3.connect('sistema_sena.db')
                cursor = conexion.cursor()
                cursor.execute('''INSERT INTO nota (
                    nota_1,
                    nota_2,
                    nota_3,
                    resultado, 
                    id_aprendiz)
                    VALUES (?, ?, ?, ?, ?)''', (
                        nv_nota_1,
                        nv_nota_2,
                        nv_nota_3,
                        nv_promedio,
                        nv_aprendiz))
                conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Nueva nota registrada con exito")
                #Mostrar registros y limpiar cajas
                self.limpiar_cajas()
                self.mostrar_notas()
                if nv_nota_1 < 70:
                    messagebox.showwarning("Advertencia", f"La nota 1 del aprendiz {nv_aprendiz} fue de {nv_nota_1}, por lo tanto queda en plan de mejoramiento")
                elif nv_nota_2 < 70:
                    messagebox.showwarning("Advertencia", f"La nota 2 del aprendiz {nv_aprendiz} fue de {nv_nota_2}, por lo tanto queda en plan de mejoramiento")
                elif nv_nota_3 < 70:
                    messagebox.showwarning("Advertencia", f"La nota 3 del aprendiz {nv_aprendiz} fue de {nv_nota_3}, por lo tanto queda en plan de mejoramiento")
    
    #Metodo para editar nota
    def editar_nota(self):
        try:
            if hasattr(self, 'registro_seleccionado'):
                nota = self.registro_seleccionado
                edit_aprendiz = self.lista_aprendiz.get(tk.ACTIVE)
                edit_nota_1 = int(self.txt_nota_1.get())
                edit_nota_2 = int(self.txt_nota_2.get())
                edit_nota_3 = int(self.txt_nota_3.get())
                edit_promedio = int((edit_nota_1 + edit_nota_2 + edit_nota_3) / 3)
                if edit_nota_1 > 100 or edit_nota_2 > 100 or edit_nota_3 > 100:
                    messagebox.showwarning("Advertencia", f"Debes añadir una nota igual o menor a 100")
                else:
                    if edit_aprendiz and edit_nota_1 and edit_nota_2 and edit_nota_3 and edit_promedio and nota:
                        conexion = sqlite3.connect('sistema_sena.db')
                        cursor = conexion.cursor()
                        cursor.execute('''UPDATE nota SET
                                        nota_1 = ?,
                                        nota_2 = ?,
                                        nota_3 = ?,
                                        resultado = ?,
                                        id_aprendiz = ?
                                        WHERE id_nota = ?''', (
                                            edit_nota_1,
                                            edit_nota_2,
                                            edit_nota_3,
                                            edit_promedio,
                                            edit_aprendiz,
                                            nota[0]
                                        ))
                    conexion.commit()
                conexion.close()
                messagebox.showinfo("Éxito", "Nueva nota registrada con exito")
                #Mostrar registros y limpiar cajas
                self.limpiar_cajas()
                self.mostrar_notas()
                if edit_nota_1 < 70:
                    messagebox.showwarning("Advertencia", f"La nota 1 del aprendiz {edit_aprendiz} fue de {edit_nota_1}, por lo tanto queda en plan de mejoramiento")
                elif edit_nota_2 < 70:
                    messagebox.showwarning("Advertencia", f"La nota 2 del aprendiz {edit_aprendiz} fue de {edit_nota_2}, por lo tanto queda en plan de mejoramiento")
                elif edit_nota_3 < 70:
                    messagebox.showwarning("Advertencia", f"La nota 3 del aprendiz {edit_aprendiz} fue de {edit_nota_3}, por lo tanto queda en plan de mejoramiento")
            else:
                messagebox.showwarning("Advertencia", "Primero selecciona a un aprendiz.")
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
    
    #Metodo para borrar informacion de las cajas
    def limpiar_cajas(self):
        self.txt_nota_1.delete(0, tk.END)
        self.txt_nota_2.delete(0, tk.END)
        self.txt_nota_3.delete(0, tk.END)
nota = CRUDNota()
nota.mainloop()