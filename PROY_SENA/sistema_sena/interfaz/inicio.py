import tkinter as tk
from crud_notas import CRUDNota
from crud_competencia import CRUDCompetencia

class Inicio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Sena")
        self.geometry("450x350")
        self.titulo_inicio = tk.Label(self, text='Sistema de aprendices SENA', font=('Arial', 22))
        self.titulo_inicio.pack(pady=5)

        self.subtitulo_inicio = tk.Label(self, text='¿Que deseas hacer?', font=('Arial', 15))
        self.subtitulo_inicio.pack(pady=10)
        
        self.boton_ir_nota = tk.Button(
            self, 
            text='Ver panel de notas.', 
            font=('Arial', 13), 
            width=20, 
            bg='green',
            fg="white",
            command=lambda: [self.ir_crud_notas(), self.cerrar_ventana()]
            )
        self.boton_ir_nota.pack(pady=5)
        
        self.boton_ir_programa = tk.Button(
            self, 
            text='Ver panel de programas.', 
            font=('Arial', 13), 
            width=20, 
            bg='green',
            fg="white",
            command=lambda: [self.ir_crud_programa(), self.cerrar_ventana()]
            )
        self.boton_ir_programa.pack(pady=5)

    def ir_crud_notas(self):
        crud_notas = CRUDNota(self)
        crud_notas.mainloop()
    
    def ir_crud_programa(self):
        crud_programa = CRUDCompetencia(self)
        crud_programa.mainloop()
    
    def cerrar_ventana(self):
        self.destroy()


inicio = Inicio()
inicio.mainloop()