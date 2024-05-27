import tkinter as tk
from tkinter import ttk
import cx_Oracle

class ModuloOpcionMultiple(tk.Frame):
    def __init__(self, parent, controller,idpreguntaEvaluacion):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.preguntaEvaluacion = idpreguntaEvaluacion
        self.opcion_var = tk.StringVar()
        self.create_widgets()

    def create_widgets(self):
        consulta = "SELECT " \
            "PEA.IDPREGUNTAEVALUACIONALUMNO,RP.OPCION " \
            "FROM PREGUNTAEVALUACIONALUMNO PEA " \
            "JOIN PREGUNTAEVALUACION PE ON PEA.IDPREGUNTAEVALUACION=PE.IDPREGUNTAEVALUACION " \
            "JOIN PREGUNTA P ON PE.IDPREGUNTA=P.IDPREGUNTA " \
            "JOIN RESPUESTAPREGUNTA RP ON RP.IDPREGUNTA=P.IDPREGUNTA "\
            "WHERE PEA.IDPREGUNTAEVALUACIONALUMNO= '" + str(self.preguntaEvaluacion) + "'"
        
        
        
        opciones = self.opcionesPregunta(consulta)
        
        
        for opcion in opciones:
            
            op= ttk.Radiobutton(self, text=opcion[1], variable=self.opcion_var,value=opcion[1])
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
    app = ModuloOpcionMultiple()
    app.mainloop()