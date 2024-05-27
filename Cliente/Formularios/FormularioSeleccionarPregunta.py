import tkinter as tk
from tkinter import ttk
import cx_Oracle
from FormularioCreacionEvaluacion import CreateEvaluationApp

class SelectQuestions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.tuplaCols = ()
        self.controller = controller

        #label = ttk.Label(self, text="Select Questions")
       # label.grid(row=0, column=0, padx=10, pady=10)

        button = ttk.Button(self, text="Cambiar vista",
                             command=lambda: controller.show_frame(CreateEvaluationApp))
        button.grid(row=1, column=0, padx=10, pady=10)
        
        button1 = ttk.Button(self, text="seleccion",
                             command=lambda: self.seleccion())
        button1.grid(row=2, column=0, padx=10, pady=10)

        # Crear y configurar el treeview
        treeFrame = ttk.Frame(self)
        treeFrame.grid(row=2, column=0, pady=10)
        
         # Centrar el treeFrame en la pantalla
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        treeframe_width = treeFrame.winfo_reqwidth()
        treeframe_height = treeFrame.winfo_reqheight()
        x = (screen_width // 5) - (treeframe_width //30)
        y = (screen_height // 25) - (treeframe_height // 25)
        treeFrame.place(x=x, y=y)
        
        
        treeScroll = ttk.Scrollbar(treeFrame)
        treeScroll.pack(side="right", fill="y")
        screenHeight = self.winfo_screenheight() // 25
        cols = ("ENUNCIADO", "TIPO", "TEMA", "NOMBREDOCENTE")
        self.treeview = ttk.Treeview(treeFrame, show="headings", yscrollcommand=treeScroll.set, columns=cols, height=screenHeight)
        
        
        
        
        
        self.cargarPreguntas()
        self.treeview.pack()
        treeScroll.config(command=self.treeview.yview)

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
        selectedItems=self.treeview.selection()
        
        for item in selectedItems:
            currentItem=self.treeview.item(item)
            currentValues=currentItem.get("values")
            