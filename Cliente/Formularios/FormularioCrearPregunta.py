import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
import ttkbootstrap as tb
import sys
sys.path.insert(0,'C:/Users/Crist/OneDrive/Documentos/FrontExamenQuizBd2/Cliente/SpecialWidgets')
from  DigitalClock import get_time    

sys.path.insert(0,'C:/Users/Crist/OneDrive/Documentos/FrontExamenQuizBd2/Cliente/PeticionesCombobox')
from PeticionesComboboxServidor import opcionesComboBox

class CreateQuestion(tk.Frame):
    
  
     
    def __init__(self, parent, controller,dni,rol,nombre): 
        tk.Frame.__init__(self, parent)
        #self.title("Creación de evaluación")
        #self.geometry("800x650")
        #self.resizable(True, True)
        self.controller = controller
        self.dni = dni
        self.rol = rol
        self.nombre = nombre



        # Crear los marcos principales
        self.create_main_frames()

        # Crear los widgets de información de la evaluación
        self.create_question_info_widgets()

      

        # Crear el botón de creación de evaluación
        self.create_create_button()


    
     
     
    def create_main_frames(self):
        from FormularioSeleccionarPregunta import SelectQuestions

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=20, pady=0)
        
           # Crear un nuevo marco para el botón "Regresar"
        self.top_frame = ttk.Frame(self.main_frame)
        self.top_frame.pack(side="top", fill="x")

        # Crear el botón "Regresar" y agregarlo al nuevo marco
        button_regresar = ttk.Button(self.top_frame, text="Regresar", command=lambda: self.show_frame(SelectQuestions))
        button_regresar.pack(side="top",pady=0)
        
        
        self.title_label = ttk.Label(self.main_frame, text="Creación de pregunta", font=("Arial", 17, "bold"))
        self.title_label.pack(pady=0)

        self.pregunta_info_frame = ttk.LabelFrame(self.main_frame, text="Información de la pregunta")
        self.pregunta_info_frame.pack(padx=20, pady=10, fill="x")

        self.pregunta_details_frame = ttk.LabelFrame(self.main_frame, text="Detalles de la pegunta")
        self.pregunta_details_frame.pack(padx=20, pady=10, fill="x")

    def create_question_info_widgets(self):
        # Enunciado
        self.question_enunciado_label = ttk.Label(self.pregunta_info_frame, text="Enuncido")
        self.question_enunciado_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.question_enunciado_entry= ttk.Entry(self.pregunta_info_frame)
        self.question_enunciado_entry.grid(row=0, column=1, padx=30, pady=10)

        # Tipo pregunta
        self.tipo_pregunta_label = ttk.Label(self.pregunta_info_frame, text="Tipo pregunta")
        self.tipo_pregunta_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.tipo_pregunta_type_combobox = ttk.Combobox(self.pregunta_info_frame, values= opcionesComboBox('TIPOPREGUNTA', 'TIPO'), state="readonly")
        self.tipo_pregunta_type_combobox.grid(row=1, column=1, padx=30, pady=10)

        # Tema
        self.tema_label = ttk.Label(self.pregunta_info_frame, text="Tema")
        self.tema_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        
        self.tipo_pregunta_type_combobox = ttk.Combobox(self.pregunta_info_frame, values= opcionesComboBox('TEMA', 'TEMA'), state="readonly")
        self.tipo_pregunta_type_combobox.grid(row=2, column=1, padx=30, pady=10)
        

        # visibilidad pregunta
        self.visibilidad_pregunta_label = ttk.Label(self.pregunta_details_frame, text="Visibilidad pregunta")
        self.visibilidad_pregunta_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        
        self.visibilidad_pregunta_combobox = ttk.Combobox(self.pregunta_details_frame, values= opcionesComboBox('VISIBILIDADPREGUNTA', 'VISIBILIDAD'), state="readonly")
        self.visibilidad_pregunta_combobox.grid(row=3, column=1, padx=30, pady=10)
       
      
        
   


    def create_create_button(self):
        self.create_button = ttk.Button(self.main_frame, text="Crear pregunta", command=self.create_question)
        self.create_button.pack(pady=0)

    def create_question(self):
        # Aquí puedes agregar la lógica para crear la evaluación
        # con los datos ingresados en los widgets
        pass
    
    def show_frame(self, frame_class):
        

        frame=self.limpiar_frame()
        
        frame = frame_class(self, self.controller,self.dni,self.rol,self.nombre)
        
            
        #frame = frame_class(self, self.controller,self.dni)
        frame.pack(fill="both", expand=True) 
        
    def limpiar_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
    
     


if __name__ == "__main__":
    app = CreateQuestion()
    app.mainloop()