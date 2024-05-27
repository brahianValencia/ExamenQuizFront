import tkinter as tk
from tkinter import ttk
import cx_Oracle

#Aquí la consulta será para validar si lo ingresado por el usuario es o no correcto
class ModuloRellenarEspacios(tk.Frame):
    def __init__(self, parent, controller, pregunta):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.preguntaEvaluacion = pregunta
        self.create_widgets()

    def create_widgets(self):
        # Procesar el texto y crear la interfaz
        self.entries = []
        parts = self.preguntaEvaluacion.split("{}")

        frame_labels = tk.Frame(self)
        frame_labels.pack(side=tk.TOP, fill=tk.X)

        frame_entries = tk.Frame(self)
        frame_entries.pack(side=tk.TOP, fill=tk.X)

        for i, part in enumerate(parts):
            if part:
                label = tk.Label(frame_labels, text=part)
                label.pack(fill='both',anchor='center')

            if i < len(parts) - 1:
                entry = tk.Entry(frame_entries)
                entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
                self.entries.append(entry)

        boton_responder = ttk.Button(self, text="Responder")
        boton_responder.pack(pady=10)

    def opcionesPregunta(self, consulta):
        connectStr = 'examenquiz/123@localhost:1521/xepdb1'
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
    app = ModuloRellenarEspacios()
    app.mainloop()