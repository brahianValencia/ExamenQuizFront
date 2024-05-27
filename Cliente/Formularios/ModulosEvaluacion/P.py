import tkinter as tk
from tkinter import messagebox

class DragAndDropQuestion:
    def __init__(self, root):
        self.root = root
        self.root.title("Drag and Drop Question")

        # Pregunta
        self.question_label = tk.Label(root, text="Ordena los números del 1 al 3:", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        # Crear slots
        self.slots = [tk.Frame(root, width=100, height=50, bd=1, relief="sunken") for _ in range(3)]
        self.slot_positions = [(200, 100), (200, 160), (200, 220)]
        for slot, pos in zip(self.slots, self.slot_positions):
            slot.place(x=pos[0], y=pos[1])

        # Crear etiquetas arrastrables
        self.labels = [
            tk.Label(root, text="3", bg="lightblue", width=10),
            tk.Label(root, text="1", bg="lightgreen", width=10),
            tk.Label(root, text="2", bg="lightcoral", width=10)
        ]

        # Guardar posiciones y tamaños originales
        self.original_positions = [(50, 100), (50, 160), (50, 220)]
        self.original_sizes = [(label.winfo_reqwidth(), label.winfo_reqheight()) for label in self.labels]

        # Posicionar etiquetas
        for label, pos in zip(self.labels, self.original_positions):
            label.place(x=pos[0], y=pos[1])
            label.bind("<Button-1>", self.on_drag_start)
            label.bind("<B1-Motion>", self.on_drag_motion)
            label.bind("<ButtonRelease-1>", self.on_drop)

        # Botón para validar el orden
        self.validate_button = tk.Button(root, text="Validar", command=self.validate_order)
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

    def validate_order(self):
        # Obtener las posiciones de las etiquetas en los slots
        slot_contents = {}
        for slot in self.slots:
            for label in self.labels:
                if (slot.winfo_x() == label.winfo_x() and slot.winfo_y() == label.winfo_y()):
                    slot_contents[slot.winfo_y()] = label.cget("text")

        # Verificar el orden basado en las posiciones de los slots
        expected_order = ["1", "2", "3"]
        actual_order = [slot_contents.get(pos[1], "") for pos in self.slot_positions]

        if actual_order == expected_order:
            messagebox.showinfo("Resultado", "¡Correcto!")
        else:
            messagebox.showerror("Resultado", "Incorrecto. Inténtalo de nuevo.")

if __name__ == "__main__":
    root = tk.Tk()
    app = DragAndDropQuestion(root)
    root.mainloop()
