
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb



class App(tk.Tk):
# __init__ function for class tkinterApp 
    def __init__(self, *args, **kwargs): 
        from FormularioCursos import CursosApp
        from FormularioUsuarios import NombresDB

         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
         
        # creating a container
        container = tk.Frame(self)  
        container.pack(side = "top", fill = "both", expand = True) 
  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
  
        # initializing frames to an empty array
        self.frames = {}  
  
        # iterating through a tuple consisting
        # Crear las pestañas
        for F in (NombresDB, CursosApp):
            if F == CursosApp:
                frame = F(container, self, "","","")  # Pasar un valor temporal para dni y para nombre
            else:
                frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
  
        #frame.grid(row = 5, column = 0, sticky ="nsew")
  
        self.show_frame(NombresDB)
  
    # to display the current frame passed as
    # parameter
    
    
    def show_frame(self, cont):
        from FormularioCursos import CursosApp

        frame = self.frames[cont]
        frame.tkraise()
        if cont == CursosApp:
            frame.set_dni(self.dni_nombre_seleccionado)
            
    
        
if __name__ == "__main__":
    app = App()
    app.mainloop()