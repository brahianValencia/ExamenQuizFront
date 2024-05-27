import tkinter as tk
from tkinter import ttk
import cx_Oracle
#Aquí la consulta es para validar si lo que yo ingresé como respuesta es correcto o no
class ModuloVerdaderoFalso(tk.Frame):
    def __init__(self, parent, controller,idpreguntaEvaluacion):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.preguntaEvaluacion = idpreguntaEvaluacion
        self.opcion_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        
  
            
            op= ttk.Radiobutton(self, text="Verdadero", variable=self.opcion_var,value="Verdadero")
            op.pack(pady=5)
            
            op= ttk.Radiobutton(self, text="Falso", variable=self.opcion_var,value="Falso")
            op.pack(pady=10)
            
            boton_responder = ttk.Button(self, text="Responder")
            boton_responder.pack(pady=15)

        
        
        
            
            
        

        
        
        

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
    app = ModuloVerdaderoFalso()
    app.mainloop()