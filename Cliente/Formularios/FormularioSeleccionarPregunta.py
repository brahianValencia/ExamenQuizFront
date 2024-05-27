import tkinter as tk
from tkinter import ttk
import cx_Oracle

class SelectQuestions(tk.Frame):
    def __init__(self, parent, controller, dni, rol, nombre):
        from FormularioCreacionEvaluacion import CreateEvaluation
        from FormularioCrearPregunta import CreateQuestion


        tk.Frame.__init__(self, parent)
        self.tuplaCols = ()
        self.controller = controller
        self.dni = dni
        self.rol = rol
        self.nombre = nombre
        
        self.selected_values = []
        
        
        # Crear el frame principal
        main_frame = ttk.Frame(self)
        main_frame.pack(fill="x", expand=True)

        # Crear el frame para los botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(side="top", fill="x", pady=10)

        button = ttk.Button(button_frame, text="Regresar", command=lambda: self.show_frame(CreateEvaluation))
        button.pack(side="left", padx=10)

        button1 = ttk.Button(button_frame, text="Seleccionar", command=lambda: self.seleccion())
        button1.pack(side="left", padx=10)
        
        button2 = ttk.Button(button_frame, text="Crear pregunta",command=lambda: self.show_frame(CreateQuestion))
        button2.pack(side="left", padx=10)
        
        

        # Crear el frame para la primera tabla
        first_table_frame = ttk.Frame(main_frame)
        first_table_frame.pack(side="top", fill="x")

        # Crear y configurar el treeview para la primera tabla
        treeScroll = ttk.Scrollbar(first_table_frame)
        treeScroll.pack(side="right", fill="y")
        screenHeight = self.winfo_screenheight() // 40
        cols = ("IDPREGUNTA", "ENUNCIADO", "TIPO", "TEMA", "NOMBREDOCENTE")
        self.treeview = ttk.Treeview(first_table_frame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=screenHeight)
        self.cargarPreguntas()
        self.treeview.pack(side="left", fill="both", expand=True)
        treeScroll.config(command=self.treeview.yview)

        # Crear el frame para la segunda tabla
        second_table_frame = ttk.Frame(main_frame)
        second_table_frame.pack(side="bottom", fill="x")

        # Crear el treeview para la segunda tabla
        self.second_treeview = ttk.Treeview(second_table_frame, columns=self.tuplaCols, show="headings")
        self.second_treeview.pack(side="left", fill="both", expand=True)

        # Configurar las cabeceras de la segunda tabla
        for col in self.tuplaCols:
            self.second_treeview.heading(col, text=col)

    def cargarNombresColumnas(self, table_name):
        connectStr = 'examenquiz/123@localhost:1521/xepdb1'
        connection = cx_Oracle.connect(connectStr)
        cursor = connection.cursor()
        cursor.execute(f"SELECT column_name FROM user_tab_columns WHERE table_name = '{table_name}'")
        values = cursor.fetchall()
        arrayValues = [row for row in values]
        stringarrayValues = [str(elem) for row in arrayValues for elem in row]
        self.tuplaCols = tuple(stringarrayValues)
        stringFromArray = ', '.join(stringarrayValues)
        cursor.close()
        connection.close()
        return stringFromArray

    def cargarPreguntas(self):
        connectStr = 'examenquiz/123@localhost:1521/xepdb1'
        connection = cx_Oracle.connect(connectStr)
        cursor = connection.cursor()
        cursor.execute(f"SELECT {self.cargarNombresColumnas('VISTAPREGUNTA')} FROM VISTAPREGUNTA")
        values = cursor.fetchall()
        ArrayValues = [row for row in values]
        for row in self.tuplaCols:
            self.treeview.heading(row, text=row)
        for row in ArrayValues:
            self.treeview.insert('', 'end', values=row)
        cursor.close()
        connection.close()
        return ArrayValues
    
    def seleccion(self):
        selectedItems = self.treeview.selection()
        # Limpiar la segunda tabla antes de cargar las nuevas preguntas
        #for item in self.second_treeview.get_children():
        #    self.second_treeview.delete(item)

        values = [self.second_treeview.item(item)['values'] for item in self.second_treeview.get_children()]

        # Obtener los valores de las preguntas seleccionadas
        self.selected_values = [self.treeview.item(item)['values'] for item in selectedItems]

        # Cargar las preguntas seleccionadas en la segunda tabla
        for values_row in self.selected_values:
            if values_row not in values:
                self.second_treeview.insert('', 'end', values=values_row)

    def cargar_preguntas_seleccionadas(self, selectedItems):
        for item in selectedItems:
            currentItem = self.treeview.item(item)
            currentValues = currentItem.get("values")
            self.second_treeview.insert('', 'end', values=currentValues)
            
    def show_frame(self, frame_class):
       # from FormularioCreacionEvaluacion import CreateEvaluation

        frame=self.limpiar_frame()
        frame = frame_class(self, self.controller,self.dni,self.rol,self.nombre)
        frame.pack(fill="both", expand=True)
            
    def limpiar_frame(self):
        for widget in self.winfo_children():
            widget.destroy()
            
if __name__ == "__main__":
    app = SelectQuestions()
    app.mainloop()