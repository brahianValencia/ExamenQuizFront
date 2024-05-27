import tkinter as tk
from tkinter import ttk
import cx_Oracle

#Aquí la consulta será para validar si lo ingresado por el usuario es o no correcto
class ModuloRespuestaCorta(tk.Frame):
    def __init__(self, parent, controller,idpreguntaEvaluacion):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.preguntaEvaluacion = idpreguntaEvaluacion
        
        self.create_widgets()

    def create_widgets(self):
        
            
        op= ttk.Entry(self)
        op.pack(pady=5)

        boton_responder = ttk.Button(self, text="Responder")
        boton_responder.pack(pady=10)
            
            
        

        
        
        

    def opcionesPregunta(self,consulta):
        connectStr='examenquiz/123@localhost:1521/xepdb1'
        connection = cx_Oracle.connect(connectStr)
        cursor = connection.cursor()
        
        
                    
        cursor.execute(consulta)
        values = cursor.fetchall()
        # Crear una lista con los valores de la columna
        ArrayValues = [row for row in values]
        
        

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()  
        return ArrayValues

if __name__ == "__main__":
    app = ModuloRespuestaCorta()
    app.mainloop()