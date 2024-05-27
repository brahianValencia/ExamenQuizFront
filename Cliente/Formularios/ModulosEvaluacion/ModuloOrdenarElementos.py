import tkinter as tk
from tkinter import ttk,messagebox
import cx_Oracle

class ModuloOrdenarElementos(tk.Frame):
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

        # Pregunta
        self.question_label = tk.Label(self, text="Ordena las opciones:", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        # Crear slots
        self.slots = [tk.Frame(self, width=100, height=50, bd=1, relief="sunken") for _ in range(len(opciones))]
        self.slot_positions = [(200, 100 + 60 * i) for i in range(len(opciones))]
        for slot, pos in zip(self.slots, self.slot_positions):
            slot.place(x=pos[0], y=pos[1])

        # Crear etiquetas arrastrables
        self.labels = [tk.Label(self, text=opcion[1], bg="lightblue", width=10) for opcion in opciones]

        # Guardar posiciones y tamaños originales
        self.original_positions = [(50, 100 + 60 * i) for i in range(len(opciones))]
        self.original_sizes = [(label.winfo_reqwidth(), label.winfo_reqheight()) for label in self.labels]

        # Posicionar etiquetas
        for label, pos in zip(self.labels, self.original_positions):
            label.place(x=pos[0], y=pos[1])
            label.bind("<Button-1>", self.on_drag_start)
            label.bind("<B1-Motion>", self.on_drag_motion)
            label.bind("<ButtonRelease-1>", self.on_drop)

        # Botón para validar el orden
        self.validate_button = tk.Button(self, text="Validar", command=self.validate_order)
        self.validate_button.pack(pady=20)

        # Variable para guardar la posición inicial del clic
        self.drag_data = {"x": 0, "y": 0, "item": None}

    def on_drag_start(self, event):
        # Guardar la posición inicial
        self.drag_data["item"] = event.widget
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_drag_motion(self, event):
        # Calcular el desplazamiento
        delta_x = event.x - self.drag_data["x"]
        delta_y = event.y - self.drag_data["y"]

        # Mover el widget
        x = self.drag_data["item"].winfo_x() + delta_x
        y = self.drag_data["item"].winfo_y() + delta_y
        self.drag_data["item"].place(x=x, y=y)

    def on_drop(self, event):
        widget = self.drag_data["item"]
        widget_x, widget_y = widget.winfo_x(), widget.winfo_y()

        # Verificar si el widget está dentro de algún slot
        dropped_in_slot = False
        for slot in self.slots:
            slot_x, slot_y = slot.winfo_x(), slot.winfo_y()
            slot_width, slot_height = slot.winfo_width(), slot.winfo_height()

            if (slot_x < widget_x < slot_x + slot_width and
                slot_y < widget_y < slot_y + slot_height):
                # Posicionar y redimensionar el widget dentro del slot
                widget.place(x=slot_x, y=slot_y, width=slot_width, height=slot_height)
                dropped_in_slot = True
                break

        if not dropped_in_slot:
            # Restaurar posición y tamaño original si no está en un slot
            index = self.labels.index(widget)
            orig_pos = self.original_positions[index]
            orig_size = self.original_sizes[index]
            widget.place(x=orig_pos[0], y=orig_pos[1], width=orig_size[0], height=orig_size[1])
     
    '''
    def validate_order(self):
        # Obtener las posiciones de las etiquetas en los slots
        slot_contents = {}
        for slot in self.slots:
            for label in self.labels:
                if (slot.winfo_x() == label.winfo_x() and slot.winfo_y() == label.winfo_y()):
                    slot_contents[slot.winfo_y()] = label.cget("text")

        # Verificar el orden basado en las posiciones de los slots
        expected_order = [opcion[1] for opcion in sorted(self.opcionesPregunta(consulta), key=lambda x: x[0])]
        actual_order = [slot_contents.get(pos[1], "") for pos in self.slot_positions]

        if actual_order == expected_order:
            messagebox.showinfo("Resultado", "¡Correcto!")
        else:
            messagebox.showerror("Resultado", "Incorrecto. Inténtalo de nuevo.")
    '''   

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
    app = ModuloOrdenarElementos()
    app.mainloop()