import tkinter as tk
from tkinter import messagebox
import sqlite3

class CRUDNota(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Panel de Notas")

        # Etiquetas y campos de entrada para los datos de la nota
        self.lbl_nota = tk.Label(self, text="Nota:")
        self.lbl_nota.grid(row=0, column=0, sticky="w")
        self.entry_nota = tk.Entry(self)
        self.entry_nota.grid(row=0, column=1)

        # Botones para realizar operaciones CRUD
        self.btn_agregar = tk.Button(self, text="Agregar", command=self.agregar_nota)
        self.btn_agregar.grid(row=1, column=0, pady=5)
        self.btn_actualizar = tk.Button(self, text="Actualizar", command=self.actualizar_nota)
        self.btn_actualizar.grid(row=1, column=1, pady=5)
        self.btn_eliminar = tk.Button(self, text="Eliminar", command=self.eliminar_nota)
        self.btn_eliminar.grid(row=1, column=2, pady=5)

        # Lista para mostrar las notas existentes
        self.lista_notas = tk.Listbox(self, width=50)
        self.lista_notas.grid(row=2, columnspan=3, pady=5)

        # Cargar las notas existentes al iniciar la aplicación
        self.cargar_notas()

    def cargar_notas(self):
        self.lista_notas.delete(0, tk.END)  # Limpiar la lista
        # Conectar a la base de datos y obtener las notas
        conexion = sqlite3.connect('sistema_sena.db')
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM nota")
        notas = cursor.fetchall()
        conexion.close()
        # Agregar las notas a la lista
        for nota in notas:
            self.lista_notas.insert(tk.END, nota[0])  # Solo mostramos el ID de la nota

    def agregar_nota(self):
        # Obtener la nota ingresada por el usuario
        nueva_nota = self.entry_nota.get().strip()
        if nueva_nota:
            # Conectar a la base de datos y agregar la nueva nota
            conexion = sqlite3.connect('sistema_sena.db')
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO nota (nota) VALUES (?)", (nueva_nota,))
            conexion.commit()
            conexion.close()
            # Actualizar la lista de notas
            self.cargar_notas()
            messagebox.showinfo("Éxito", "Nota agregada correctamente.")
            # Limpiar el campo de entrada
            self.entry_nota.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor ingresa una nota.")

    def actualizar_nota(self):
        # Obtener la nota seleccionada en la lista
        seleccion = self.lista_notas.curselection()
        if seleccion:
            indice = seleccion[0]
            nueva_nota = self.entry_nota.get().strip()
            if nueva_nota:
                # Conectar a la base de datos y actualizar la nota
                id_nota = self.lista_notas.get(indice)
                conexion = sqlite3.connect('sistema_sena.db')
                cursor = conexion.cursor()
                cursor.execute("UPDATE nota SET nota = ? WHERE id_nota = ?", (nueva_nota, id_nota))
                conexion.commit()
                conexion.close()
                # Actualizar la lista de notas
                self.cargar_notas()
                messagebox.showinfo("Éxito", "Nota actualizada correctamente.")
            else:
                messagebox.showerror("Error", "Por favor ingresa una nota válida.")
        else:
            messagebox.showerror("Error", "Por favor selecciona una nota de la lista.")

    def eliminar_nota(self):
        # Obtener la nota seleccionada en la lista
        seleccion = self.lista_notas.curselection()
        if seleccion:
            id_nota = self.lista_notas.get(seleccion[0])
            # Confirmar eliminación con el usuario
            confirmacion = messagebox.askyesno("Confirmar", "¿Estás seguro de que quieres eliminar esta nota?")
            if confirmacion:
                # Conectar a la base de datos y eliminar la nota
                conexion = sqlite3.connect('sistema_sena.db')
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM nota WHERE id_nota = ?", (id_nota,))
                conexion.commit()
                conexion.close()
                # Actualizar la lista de notas
                self.cargar_notas()
                messagebox.showinfo("Éxito", "Nota eliminada correctamente.")
        else:
            messagebox.showerror("Error", "Por favor selecciona una nota de la lista.")


