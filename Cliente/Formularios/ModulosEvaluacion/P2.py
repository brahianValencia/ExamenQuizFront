import tkinter as tk
from tkinter import messagebox

class FillInQuestions:
    def __init__(self, root, text):
        self.root = root
        self.root.title("Fill in the Blanks")

        # Frame para contener el texto y los campos de entrada
        self.text_frame = tk.Frame(root)
        self.text_frame.pack(pady=20, padx=20)

        # Procesar el texto y crear la interfaz
        self.entries = []
        self.create_fill_in_questions(text)

        # Botón para validar respuestas
        self.validate_button = tk.Button(root, text="Validar", command=self.validate_answers)
        self.validate_button.pack(pady=20)

    def create_fill_in_questions(self, text):
        parts = text.split("{}")
        row, col = 0, 0

        for i, part in enumerate(parts):
            if part:
                label = tk.Label(self.text_frame, text=part)
                label.grid(row=row, column=col, sticky='w')
                col += 1
            
            if i < len(parts) - 1:
                entry = tk.Entry(self.text_frame)
                entry.grid(row=row, column=col, sticky='w')
                self.entries.append(entry)
                col += 1

    def validate_answers(self):
        # Aquí puedes agregar la lógica para validar las respuestas
        # Por ejemplo, obtener el texto de cada entry y comprobar si es correcto
        answers = [entry.get() for entry in self.entries]
        messagebox.showinfo("Respuestas", f"Las respuestas ingresadas son: {answers}")

if __name__ == "__main__":
    root = tk.Tk()
    text = "Complete los espacios en blanco: {} es el capital de Francia. {} es el capital de Alemania."
    app = FillInQuestions(root, text)
    root.mainloop()
