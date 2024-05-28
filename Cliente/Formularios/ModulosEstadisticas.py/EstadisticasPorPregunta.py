import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Label en Treeview")

        # Crear Treeview
        self.tree = ttk.Treeview(root, columns=('A', 'B', 'C'), show='headings')
        self.tree.heading('A', text='Columna A')
        self.tree.heading('B', text='Columna B')
        self.tree.heading('C', text='Etiqueta')
        self.tree.pack(fill=tk.BOTH, expand=True)

        # Insertar una fila
        self.tree.insert('', 'end', values=('Fila 1', 'Datos 1', ''))

        # Crear Label
        self.label = tk.Label(root, text="Etiqueta de ejemplo", bg='lightgrey')

        # Vincular evento de clic en el Treeview
        self.tree.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        # Posicionar el Label dentro de la celda solo cuando se hace clic en una celda
        bbox = self.tree.bbox(self.tree.identify_row(event.y), column=2)
        if bbox:
            self.label.place(x=bbox[0], y=bbox[1], width=bbox[2], height=bbox[3])

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
