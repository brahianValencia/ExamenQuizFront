import tkinter as tk
from tkinter import ttk
import cx_Oracle
from FormularioEvaluacionesCurso import FormularioCursoEvaluaciones
from FormularioCreacionEvaluacion import CreateEvaluation
class CursosApp(tk.Frame):
    def __init__(self, parent, controller,dni,rol,nombre):

        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        self.dni = dni  # Almacenar el parámetro recibido
        self.rol=rol
        self.nombre=nombre
        self.parent = parent
        self.selected_curso = None
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True)
        self.create_widgets()

  
    
    def create_widgets(self):
        from FormularioUsuarios import NombresDB

        # Frame principal
        main_frame = ttk.Frame(self.notebook)
        
        
        # Label y ComboBox de alumnos
        label_rol = ttk.Label(main_frame, text="Inició sesión como "+str.capitalize(self.rol)+".")
        label_rol.pack(pady=10)
        
        label_usuario = ttk.Label(main_frame, text="Nombre usuario: "+self.nombre+".")
        label_usuario.pack(pady=10)
        
        
         # Crear el botón "Regresar"
        button_regresar = ttk.Button(self, text="Regresar", command=lambda: self.show_frame(NombresDB))
        button_regresar.pack(pady=20)
        
        
        self.notebook.add(main_frame, text="Cursos")
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

       
        
        
        
        consulta = "SELECT C.NOMBRE, C.DESCRIPCION, D.NOMBRES||' '||D.APELLIDOS AS NOMBRE_DOCENTE " \
           "FROM ALUMNOGRUPOCURSO AGC " \
           "JOIN GRUPOCURSO GC ON GC.IDGRUPOCURSO = AGC.IDGRUPOCURSO " \
           "JOIN CURSO C ON C.IDCURSO = GC.IDCURSO " \
           "JOIN DOCENTE D ON GC.DOCENTE_DNI = D.DNI " \
           "JOIN ALUMNOGRUPOCURSO AGC ON AGC.IDGRUPOCURSO = GC.IDGRUPOCURSO AND AGC.ALUMNO_DNI =  '" + self.dni + "'"
        
        if self.rol=='DOCENTE':
           consulta = "SELECT C.NOMBRE, C.DESCRIPCION, D.NOMBRES||' '||D.APELLIDOS AS NOMBRE_DOCENTE " \
           "FROM GRUPOCURSO GC  " \
           "JOIN CURSO C ON C.IDCURSO = GC.IDCURSO " \
           "JOIN DOCENTE D ON GC.DOCENTE_DNI = D.DNI   AND D.DNI  =  '" + self.dni + "'"
           
           boton_crear_examnen = ttk.Button(main_frame, text="Crear Examen",command=lambda: self.show_frame(CreateEvaluation))
           boton_crear_examnen.pack(anchor="ne", padx=20, pady=20)
        
        cursos= self.mostrar_cursos(consulta)
        
        # Crear recuadros para cada curso
        self.curso_frames = []
        for i, curso in enumerate(cursos):
            curso_frame = ttk.LabelFrame(main_frame, text=curso[0], cursor="hand2")
            curso_frame.pack(pady=10, fill="x")
            curso_frame.bind("<Button-1>", lambda event, curso_index=i: self.show_curso_details(curso_index))

            # Agregar contenido al recuadro del curso
            contenido_curso = ttk.Label(curso_frame, text=curso[1])
            contenido_curso.pack(padx=10, pady=10)
            contenido_curso.bind("<Button-1>", lambda event, curso_index=i: self.show_curso_details(curso_index))

            
            #Agregar el profesor que la dicta
            contenido_curso = ttk.Label(curso_frame, text="Profesor: "+curso[2])
            contenido_curso.pack(padx=10, pady=10)
            contenido_curso.bind("<Button-1>", lambda event, curso_index=i: self.show_curso_details(curso_index))

            
            self.curso_frames.append(curso_frame)

    def show_curso_details(self, curso_index):
        # Deseleccionar el curso previamente seleccionado
        if self.selected_curso is not None:
            self.curso_frames[self.selected_curso].configure(relief="raised")

        # Seleccionar el nuevo curso
        self.selected_curso = curso_index
        self.curso_frames[curso_index].configure(relief="sunken")

        # Crear una nueva pestaña para mostrar los detalles del curso
        
        curso_details_frame = self.show_frame(FormularioCursoEvaluaciones)
     
        
    def mostrar_cursos(self,consulta):
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
    
    def show_frame(self, frame_class):
        from FormularioUsuarios import NombresDB

        frame=self.limpiar_frame()
        if frame_class==NombresDB:
            frame = frame_class(self, self.controller)
        elif frame_class!=CreateEvaluation:
            frame = frame_class(self, self.controller,self.dni,self.rol,self.nombre)
        else: 
            frame = frame_class(self, self.controller,self.dni,self.rol,self.nombre)
            
        #frame = frame_class(self, self.controller,self.dni)
        frame.pack(fill="both", expand=True) 
        
    def limpiar_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
 
    
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Cursos")
    app = CursosApp(ventana, None)
    app.pack(fill="both", expand=True)
    #ventana.mainloop()