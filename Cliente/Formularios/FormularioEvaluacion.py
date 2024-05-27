import tkinter as tk
from tkinter import ttk
import cx_Oracle
from datetime import datetime

from ModulosEvaluacion.ModuloOpcionMultiple import ModuloOpcionMultiple
from ModulosEvaluacion.ModuloOrdenarElementos import ModuloOrdenarElementos
from ModulosEvaluacion.ModuloRespuestaCorta import ModuloRespuestaCorta
from ModulosEvaluacion.ModuloVerdaderoFalso import ModuloVerdaderoFalso
from ModulosEvaluacion.ModuloRellenarEspacios  import ModuloRellenarEspacios
from ModulosEvaluacion.CuentaRegresivaEvaluacion import CountdownApp
#from ModulosEvaluacion.ModuloRelacionarElementos import ModuloRelacionarElementos



class FormularioEvaluacion(tk.Frame):
    def __init__(self, parent, controller,dni,idevaluacion,rol,nombre,duracionevaluacion):
        tk.Frame.__init__(self, parent)
        
        self.parent = parent
        self.dni=dni
        self.idevaluacion=idevaluacion
        self.controller=controller
        self.rol=rol
        self.nombre=nombre
        self.duracionevaluacion=duracionevaluacion
        self.create_widgets()

        
    def create_widgets(self):
        from FormularioEvaluacionesCurso import FormularioCursoEvaluaciones
        # Iniciar la cuenta regresiva
        
      
        countdown_minutes = self.duracionevaluacion  # Duración de la cuenta regresiva en minutos
        self.countdown_app = CountdownApp(self, countdown_minutes)
        self.countdown_app.pack(side="right", pady=0)
        consulta = "SELECT DISTINCT " \
            "P.ENUNCIADO,TP.TIPO,PEA.IDPREGUNTAEVALUACIONALUMNO " \
            "FROM PREGUNTAEVALUACIONALUMNO PEA " \
            "JOIN PREGUNTAEVALUACION PE ON PEA.IDPREGUNTAEVALUACION=PE.IDPREGUNTAEVALUACION " \
            "JOIN PREGUNTA P ON PE.IDPREGUNTA=P.IDPREGUNTA " \
            "JOIN TIPOPREGUNTA TP ON TP.IDTIPOPREGUNTA=P.IDTIPOPREGUNTA " \
            "JOIN RESPUESTAPREGUNTA RP ON RP.IDPREGUNTA=P.IDPREGUNTA " \
            "JOIN EVALUACIONALUMNO EA ON PEA.IDEVALUACIONALUMNO=EA.IDEVALUACIONALUMNO AND EA.IDEVALUACIONALUMNO='" + str(self.idevaluacion) + "' " \
            "JOIN ALUMNOGRUPOCURSO AGC ON EA.IDALUMNOGRUPOCURSO=AGC.IDALUMNOGRUPOCURSO AND AGC.ALUMNO_DNI= '" + self.dni + "'"
         
        
        
        
        preguntas = self.preguntas(consulta)
        
        for pregunta in preguntas:
         enunciado=self.imprimirEnunciado(pregunta[0],pregunta[1])
         opciones=self.imprimirOpcionesTipoPregunta(pregunta[1],pregunta[2],pregunta[0])
         
           # Crear el botón "Regresar"
        button_finalizar = ttk.Button(self, text="Finalizar", command=lambda: self.show_frame(FormularioCursoEvaluaciones,""))
        button_finalizar.pack(pady=20)
        

    
            
            
    def imprimirOpcionesTipoPregunta(self, tipo,idpreguntaevaluacionalumno,pregunta):
          
        if  tipo=='Opción Múltiple':
          opciones=self.show_frame(ModuloOpcionMultiple,idpreguntaevaluacionalumno)
        
        elif tipo=='Verdadero/Falso':
           pciones=self.show_frame(ModuloVerdaderoFalso,idpreguntaevaluacionalumno)  

        elif tipo=='Respuesta Corta':
          opciones=self.show_frame(ModuloRespuestaCorta,idpreguntaevaluacionalumno)  
          
        elif tipo=='Rellenar Espacios':
          opciones=self.show_frame(ModuloRellenarEspacios,pregunta)  
        elif tipo=='Ordenar Elementos':
          opciones=self.show_frame(ModuloOrdenarElementos,idpreguntaevaluacionalumno)

        elif tipo=='Relacionar elementos':
            ""
        

          
    def preguntas(self,consulta):
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
    
    def imprimirEnunciado(self,enunciado,tipo):
        if tipo!='Rellenar Espacios':
            enunciado_label = ttk.Label(self, text=enunciado, wraplength=self.winfo_screenwidth(), anchor="center")
            enunciado_label.pack(side="top", fill="x", pady=5)
        
        
    
    def show_frame(self, frame_class,idpreguntaevaluacion):
        from FormularioEvaluacionesCurso import FormularioCursoEvaluaciones
        if frame_class== FormularioCursoEvaluaciones:
          frame=self.limpiar_frame()
          frame = frame_class(self, self.controller,self.dni,self.rol,self.nombre)
        else:
            frame = frame_class(self, self.controller,idpreguntaevaluacion)
        #frame = frame_class(self, self.controller,idpreguntaevaluacion)
        frame.pack(fill="both", expand=True) 
        
    def limpiar_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

    
    
    

if __name__ == "__main__":
    app = FormularioEvaluacion()
    app.mainloop()