import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkcalendar import DateEntry
import ttkbootstrap as tb
import sys
sys.path.insert(0,'C:/Users/Crist/OneDrive/Documentos/conectarBDphp/Cliente/SpecialWidgets')
from  DigitalClock import get_time    

sys.path.insert(0,'C:/Users/Crist/OneDrive/Documentos/conectarBDphp/Cliente/PeticionesCombobox')
from PeticionesComboboxServidor import opcionesComboBox

class CreateEvaluation(tk.Frame):
    
  
     
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
        self.create_evaluation_info_widgets()

        # Crear los widgets de detalles de la evaluación
        self.create_evaluation_details_widgets()

        # Crear el botón de creación de evaluación
        self.create_create_button()


    
     
     
    def create_main_frames(self):
        from FormularioCursos import CursosApp

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(padx=20, pady=0)
        
           # Crear un nuevo marco para el botón "Regresar"
        self.top_frame = ttk.Frame(self.main_frame)
        self.top_frame.pack(side="top", fill="x")

        # Crear el botón "Regresar" y agregarlo al nuevo marco
        button_regresar = ttk.Button(self.top_frame, text="Regresar", command=lambda: self.show_frame(CursosApp))
        button_regresar.pack(side="top",pady=0)
        
        
        self.title_label = ttk.Label(self.main_frame, text="Creación de evaluación", font=("Arial", 17, "bold"))
        self.title_label.pack(pady=0)

        self.evaluation_info_frame = ttk.LabelFrame(self.main_frame, text="Información de la evaluación")
        self.evaluation_info_frame.pack(padx=20, pady=10, fill="x")

        self.evaluation_details_frame = ttk.LabelFrame(self.main_frame, text="Detalles de la evaluación")
        self.evaluation_details_frame.pack(padx=20, pady=10, fill="x")

    def create_evaluation_info_widgets(self):
        # Nombre de la evaluación
        self.evaluation_name_label = ttk.Label(self.evaluation_info_frame, text="Nombre de la evaluación")
        self.evaluation_name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.evaluation_name_entry = ttk.Entry(self.evaluation_info_frame)
        self.evaluation_name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Descripción de la evaluación
        self.description_label = ttk.Label(self.evaluation_info_frame, text="Descripción de la evaluación")
        self.description_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.description_text = tk.Text(self.evaluation_info_frame, height=5, width=30)
        self.description_text.grid(row=1, column=1, padx=10, pady=10)

        # Porcentaje en el curso
        self.percentage_label = ttk.Label(self.evaluation_info_frame, text="Porcentaje en el curso")
        self.percentage_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.percentage_entry = ttk.Entry(self.evaluation_info_frame)
        self.percentage_entry.grid(row=2, column=1, padx=10, pady=10)

        # Cantidad de preguntas para ganar
        self.questions_to_pass_label = ttk.Label(self.evaluation_info_frame, text="Cantidad de preguntas para ganar")
        self.questions_to_pass_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.questions_to_pass_entry = ttk.Entry(self.evaluation_info_frame)
        self.questions_to_pass_entry.grid(row=3, column=1, padx=10, pady=10)

        # Fecha y hora de inicio   date_pattern='yyyy-mm-dd
        self.start_date_label = ttk.Label(self.evaluation_info_frame, text="Fecha de inicio")
        self.start_date_label.grid(row=4, column=0, padx=10, pady=0, sticky="w")
        self.start_date_entry =tb.DateEntry(self.evaluation_info_frame,bootstyle="dark", dateformat='%x')  
        self.start_date_entry.grid(row=4, column=1, padx=10, pady=0)

        self.start_time_label = ttk.Label(self.evaluation_info_frame, text="Hora de inicio")
        self.start_time_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        
        self.updatable_start_time_label = ttk.Label(self.evaluation_info_frame, text="")
        self.updatable_start_time_label.grid(row=5, column=1, padx=10, pady=0, sticky="n")
        
        
        self.start_time_button = tk.Button(self.evaluation_info_frame, text="Hora", command=lambda:get_time(self.evaluation_info_frame,self.updatable_start_time_label))
        self.start_time_button.grid(row=5, column=1, padx=10, pady=10,sticky="e")

        # Fecha y hora de finalización
        self.end_date_label = ttk.Label(self.evaluation_info_frame, text="Fecha de finalización")
        self.end_date_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.end_date_entry = tb.DateEntry(self.evaluation_info_frame,bootstyle="dark", dateformat='%x')  
        self.end_date_entry.grid(row=6, column=1, padx=10, pady=0)

        self.end_time_label = ttk.Label(self.evaluation_info_frame, text="Hora de finalización")
        self.end_time_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        
        self.updatable_end_time_label = ttk.Label(self.evaluation_info_frame, text="")
        self.updatable_end_time_label.grid(row=7, column=1, padx=10, pady=0, sticky="n")
        
        self.end_time_button = tk.Button(self.evaluation_info_frame, text="Hora", command=lambda:get_time(self.evaluation_info_frame,self.updatable_end_time_label))
        self.end_time_button.grid(row=7, column=1, padx=10, pady=10,sticky="e")
        
   

    def create_evaluation_details_widgets(self):
        # Tipo de evaluación
        self.evaluation_type_label = ttk.Label(self.evaluation_details_frame, text="Tipo de evaluación")
        self.evaluation_type_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.evaluation_type_combobox = ttk.Combobox(self.evaluation_details_frame, values= opcionesComboBox('TIPOEVALUACION', 'TIPO'), state="readonly")


        self.evaluation_type_combobox.grid(row=0, column=1, padx=10, pady=0)

        # Categoría
        self.category_label = ttk.Label(self.evaluation_details_frame, text="Categoría")
        self.category_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.category_combobox = ttk.Combobox(self.evaluation_details_frame, values=opcionesComboBox('CATEGORIA', 'CATEGORIA'), state="readonly")
        self.category_combobox.grid(row=1, column=1, padx=10, pady=0)

    def create_create_button(self):
        self.create_button = ttk.Button(self.main_frame, text="Crear evaluación", command=self.create_evaluation)
        self.create_button.pack(pady=0)

    def create_evaluation(self):
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
    app = CreateEvaluation()
    app.mainloop()