import tkinter as tk
from tkinter import ttk
import cx_Oracle
from datetime import datetime

from FormularioEvaluacion import FormularioEvaluacion

class FormularioCursoEvaluaciones(tk.Frame):
    def __init__(self, parent, controller,dni,rol,nombre):
      
        tk.Frame.__init__(self, parent)
        
        
        
        self.curso_detalles = "curso_detalles"
        self.parent = parent
        self.dni=dni
        self.idevaluacion=""
        self.rol=rol
        self.nombre=nombre
        self.controller=controller
        self.duracion=0

        self.create_widgets()

        
    def create_widgets(self):
        from FormularioCursos import CursosApp
        from FormularioEditarEvaluacion import EditEvaluation


        consulta = "SELECT " \
                "E.NOMBRE,E.DESCRIPCION,E.PORCENTAJECURSO,E.CANTIDADPREGUNTASGANAR,E.CANTIDADPREGUNTASALUMNO," \
                "E.FECHAHORAINICIO,E.FECHAHORAFINALIZACION,D.NOMBRES||' '||D.APELLIDOS NOMBRE_DOCENTE,TE.TIPO,C.CATEGORIA," \
                "E.DURACION, EA.IDEVALUACIONALUMNO " \
                "FROM EVALUACIONALUMNO EA " \
                "JOIN EVALUACION E ON EA.IDEVALUACION=E.IDEVALUACION " \
                "JOIN DOCENTE D ON D.DNI=E.DOCENTE_DNI " \
                "JOIN TIPOEVALUACION TE ON E.IDTIPOEVALUACION=TE.IDTIPOEVALUACION " \
                "JOIN CATEGORIA C ON E.IDCATEGORIA=C.IDCATEGORIA " \
                "JOIN ALUMNOGRUPOCURSO AGC ON EA.IDALUMNOGRUPOCURSO=AGC.IDALUMNOGRUPOCURSO AND ALUMNO_DNI='" + self.dni + "'"
        
        if self.rol=='DOCENTE':
            consulta = "SELECT " \
                    "E.NOMBRE,E.DESCRIPCION,E.PORCENTAJECURSO,E.CANTIDADPREGUNTASGANAR,E.CANTIDADPREGUNTASALUMNO," \
                    "E.FECHAHORAINICIO,E.FECHAHORAFINALIZACION,D.NOMBRES||' '||D.APELLIDOS NOMBRE_DOCENTE,TE.TIPO,C.CATEGORIA," \
                    "E.DURACION, EA.IDEVALUACIONALUMNO " \
                    "FROM EVALUACIONALUMNO EA " \
                    "JOIN EVALUACION E ON EA.IDEVALUACION=E.IDEVALUACION " \
                    "JOIN DOCENTE D ON D.DNI=E.DOCENTE_DNI AND D.DNI='" + self.dni + "'" \
                    "JOIN TIPOEVALUACION TE ON E.IDTIPOEVALUACION=TE.IDTIPOEVALUACION " \
                    "JOIN CATEGORIA C ON E.IDCATEGORIA=C.IDCATEGORIA " 

        evaluaciones = self.mostrar_evaluaciones(consulta)

        # Crear un contenedor para las evaluaciones
        evaluaciones_frame = ttk.LabelFrame(self, text="Evaluaciones")
        evaluaciones_frame.pack(pady=10, fill="x")

        for evaluacion in evaluaciones:
   
            # Crear un marco para cada evaluación
            evaluacion_frame = ttk.Frame(evaluaciones_frame)
            evaluacion_frame.pack(pady=5, fill="x")

            # Agregar etiquetas para los detalles de la evaluación
            nombre_label = ttk.Label(evaluacion_frame, text=f"Nombre: {evaluacion[0]}", wraplength=evaluacion_frame.winfo_screenwidth(), anchor="w")
            nombre_label.pack(side="top", fill="x", padx=5)

            descripcion_label = ttk.Label(evaluacion_frame, text=f"Descripción: {evaluacion[1]}", wraplength=evaluacion_frame.winfo_screenwidth(), anchor="w")
            descripcion_label.pack(side="top", fill="x", padx=5)

            porcentaje_label = ttk.Label(evaluacion_frame, text=f"Porcentaje del curso: {evaluacion[2]}%", wraplength=evaluacion_frame.winfo_screenwidth(), anchor="w")
            porcentaje_label.pack(side="top", fill="x", padx=5)

            preguntas_ganar_label = ttk.Label(evaluacion_frame, text=f"Preguntas para ganar: {evaluacion[3]}", wraplength=evaluacion_frame.winfo_screenwidth(), anchor="w")
            preguntas_ganar_label.pack(side="top", fill="x", padx=5)

            preguntas_alumno_label = ttk.Label(evaluacion_frame, text=f"Preguntas para el alumno: {evaluacion[4]}", wraplength=evaluacion_frame.winfo_screenwidth(), anchor="w")
            preguntas_alumno_label.pack(side="top", fill="x", padx=5)

            fecha_inicio_label = ttk.Label(evaluacion_frame, text=f"Fecha y hora de inicio: {evaluacion[5].strftime('%Y-%m-%d %H:%M:%S')}", wraplength=evaluacion_frame.winfo_screenwidth(), anchor="w")
            fecha_inicio_label.pack(side="top", fill="x", padx=5)

            fecha_fin_label = ttk.Label(evaluacion_frame, text=f"Fecha y hora de finalización: {evaluacion[6].strftime('%Y-%m-%d %H:%M:%S')}", wraplength=evaluacion_frame.winfo_screenwidth(), anchor="w")
            fecha_fin_label.pack(side="top", fill="x", padx=5)

            docente_label = ttk.Label(evaluacion_frame, text=f"Docente: {evaluacion[7]}", wraplength=evaluacion_frame.winfo_screenwidth(), anchor="w")
            docente_label.pack(side="top", fill="x", padx=5)

            tipo_label = ttk.Label(evaluacion_frame, text=f"Tipo: {evaluacion[8]}", wraplength=evaluacion_frame.winfo_screenwidth(), anchor="w")
            tipo_label.pack(side="top", fill="x", padx=5)

            categoria_label = ttk.Label(evaluacion_frame, text=f"Categoría: {evaluacion[9]}", wraplength=evaluacion_frame.winfo_screenwidth(), anchor="w")
            categoria_label.pack(side="top", fill="x", padx=5)

            duracion_label = ttk.Label(evaluacion_frame, text=f"Duración: {evaluacion[10]} minutos", wraplength=evaluacion_frame.winfo_screenwidth(), anchor="w")
            duracion_label.pack(side="top", fill="x", padx=5)
            
            eval_alumno_label = ttk.Label(evaluacion_frame, text=f"id: {evaluacion[11]} ", wraplength=evaluacion_frame.winfo_screenwidth(), anchor="w")
            eval_alumno_label.pack(side="top", fill="x", padx=5)
            
            self.duracion=evaluacion[10]
            if self.rol=='DOCENTE':
                editar_evaluacion_button = ttk.Button(evaluacion_frame, text="Editar",command=lambda e=evaluacion: self.show_frame(EditEvaluation,e[11],e))
                editar_evaluacion_button.pack(side="top", fill="x", padx=25)
            else:
                evaluacion_button = ttk.Button(evaluacion_frame, text="Presentar")
                evaluacion_button.pack(side="top", fill="x", padx=25)
                
                if(datetime.now() < evaluacion[6]):
                    evaluacion_button.config(text="Evaluar", state="normal", style="TButton",command=lambda: self.show_frame(FormularioEvaluacion,evaluacion[11],[])) #Lo puede presentar
                else:
                    evaluacion_button.config(text="Evaluar", state="disabled", style="Disabled.TButton") #No lo puede presentar
            
        # Crear el botón "Regresar"
        button_regresar = ttk.Button(self, text="Regresar", command=lambda: self.show_frame(CursosApp,evaluacion[11],[]))
        button_regresar.pack(pady=20)
               
            
    

        
          
    def mostrar_evaluaciones(self,consulta):
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
    
    def show_frame(self, frame_class,idevaluacion,datosevaluacion):
        from FormularioCursos import CursosApp
        from FormularioEditarEvaluacion import EditEvaluation


        frame=self.limpiar_frame()
        if frame_class==CursosApp:
            frame = frame_class(self, self.controller,self.dni,self.rol,self.nombre)
        elif frame_class==EditEvaluation:
            frame = frame_class(self, self.controller,self.dni,self.rol,self.nombre,datosevaluacion)
        elif frame_class==FormularioEvaluacion:
            frame = frame_class(self, self.controller,self.dni,idevaluacion,self.rol,self.nombre,self.duracion)
        else:
            frame = frame_class(self, self.controller,self.dni,idevaluacion,self.rol,self.nombre)
        frame.pack(fill="both", expand=True) 
        
    def limpiar_frame(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    app = FormularioCursoEvaluaciones()
    app.mainloop()