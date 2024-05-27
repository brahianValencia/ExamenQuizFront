import tkinter as tk

def comprobar_respuesta():
    respuesta = int(entrada_respuesta.get())
    if respuesta==366:
        print("La respuesta es correcta")
    else:
        print("La respuesta es incorrecta") 
    # Aquí puedes agregar la lógica para comprobar la respuesta

root = tk.Tk()
root.title("Pregunta de Respuesta Corta")

enunciado = tk.Label(root, text="¿Cuántos días tiene un año bisiesto?")
enunciado.pack()

entrada_respuesta = tk.Entry(root)
entrada_respuesta.pack()

boton_responder = tk.Button(root, text="Responder", command=comprobar_respuesta)
boton_responder.pack()

root.mainloop()