import tkinter as tk
from tkinter import ttk
import sys
import cx_Oracle

sys.path.insert(0, 'C:/Users/Crist/OneDrive/Documentos/FrontExamenQuizBd2/Cliente/PeticionesCombobox')
from PeticionesComboboxServidor import opcionesComboBox


class NombresDB(tk.Frame):
    def __init__(self, parent,controller):
        from FormularioCursos import CursosApp

        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.flag=""
        self.nombre=""
         # Crear el ComboBox de Alumnos
        label_alumnos = ttk.Label(self, text="Alumnos")
        label_alumnos.pack(pady=0)
        self.combo_nombres_alumnos = ttk.Combobox(self, values=opcionesComboBox('ALUMNO', "NOMBRES||' '||APELLIDOS"))
        self.combo_nombres_alumnos.bind("<<ComboboxSelected>>", lambda event: self.seleccionar_nombre(event, self.combo_nombres_alumnos,"ALUMNO"))
       
        
        
        
        self.combo_nombres_alumnos.pack(pady=20)
        
       

        label_docentes = ttk.Label(self, text="Docentes")
        label_docentes.pack(pady=0)
        self.combo_nombres_docente = ttk.Combobox(self, values=opcionesComboBox('DOCENTE', "NOMBRES||' '||APELLIDOS"))
        self.combo_nombres_docente.bind("<<ComboboxSelected>>", lambda event: self.seleccionar_nombre(event, self.combo_nombres_docente,"DOCENTE"))

        #if dni_nombre_seleccionado=="":
         #   dni_nombre_seleccionado=self.obtener_dni(self.combo_nombres_alumnos.get(),"DOCENTE")

        
        
        self.combo_nombres_docente.pack(pady=20)
        
        button = ttk.Button(self, text="Iniciar sesión",
                             command=lambda: self.show_frame(CursosApp))
        button.pack(pady=20)



            
            
    def seleccionar_nombre(self, event, combobox, table_name):
        nombre_seleccionado = combobox.get()
        
        self.flag=table_name
        self.obtener_dni(nombre_seleccionado,table_name)
    
    def obtener_dni(self, nombre,table_name):
        # Conectarse a la base de datos Oracle
        connectStr='examenquiz/123@localhost:1521/xepdb1'
        connection = cx_Oracle.connect(connectStr)
        cursor = connection.cursor()
        cursor.execute(f"SELECT DNI FROM {table_name} WHERE NOMBRES||' '||APELLIDOS= '{nombre}'")
        values = cursor.fetchall()
        # Crear una lista con los valores de la columna
        #ArrayValues = [row for row in values]
        self.dni_nombre_seleccionado= str(values[0][0]) #Obtiene sólo el valor, sin la tupla
        self.nombre=nombre
        

        # Cerrar el cursor y la conexión
        cursor.close()
        connection.close()

        #return ArrayValues

    
    def show_frame(self, frame_class):
        frame=self.limpiar_frame()
        frame = frame_class(self, self.controller, self.dni_nombre_seleccionado,self.flag,self.nombre)
        frame.pack(fill="both", expand=True) 
        #frame.tkraise()
        #self.controller.show_frame(frame_class(self, self.controller, self.dni_nombre_seleccionado))
        
   
    def limpiar_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
            
            
 
        
        


# Crear la ventana principal
if __name__ == "__main__":
    ventana = tk.Tk()
    ventana.title("Seleccionar Nombre")
    app = NombresDB(ventana)
    app.pack()