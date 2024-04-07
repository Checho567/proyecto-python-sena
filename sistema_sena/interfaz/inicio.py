import tkinter as tk
from crud_notas import CRUDNota
from crud_competencia import CRUDCompetencia
from crud_actividad import CRUDActividad
from crud_aprendiz import CRUDAprendiz

class Inicio(tk.Tk):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Sistema Sena")
        self.geometry("450x350")
        self.titulo_inicio = tk.Label(self, text='Sistema de aprendices SENA', font=('Arial', 22))
        self.titulo_inicio.pack(pady=5)

        self.subtitulo_inicio = tk.Label(self, text='¿Que deseas hacer?', font=('Arial', 15))
        self.subtitulo_inicio.pack(pady=10)
        
        self.boton_ir_aprendiz = tk.Button(
            self, 
            text='Ver panel de aprendices.', 
            font=('Arial', 13), 
            width=20, 
            bg='green',
            fg="white",
            command=self.ir_crud_aprendiz
            )
        self.boton_ir_aprendiz.pack(pady=5)
        
        self.boton_ir_programa = tk.Button(
            self, 
            text='Ver panel de competencias.', 
            font=('Arial', 13), 
            width=21, 
            bg='green',
            fg="white",
            command=self.ir_crud_programa
            )
        self.boton_ir_programa.pack(pady=5)
        
        self.boton_ir_actividad = tk.Button(
            self, 
            text='Ver panel de actividades.', 
            font=('Arial', 13), 
            width=21, 
            bg='green',
            fg="white",
            command=self.ir_crud_actividad
            )
        self.boton_ir_actividad.pack(pady=5)

    def ir_crud_aprendiz(self):
        crud_aprendiz = CRUDAprendiz(self)
        crud_aprendiz.mainloop()
    
    def ir_crud_programa(self):
        crud_programa = CRUDCompetencia(self)
        crud_programa.mainloop()
        
    def ir_crud_actividad(self):
        crud_actividad = CRUDActividad(self)
        crud_actividad.mainloop()
    
    def cerrar_ventana(self):
        self.destroy()

inicio = Inicio()
inicio.mainloop()