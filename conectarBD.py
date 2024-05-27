import cx_Oracle
import os
import glob
import tkinter as tk

#from models.Clientes import Clientes

#object=Clientes(44,444,4,44,4)
#tableName="Clientes"
#columns = ', '.join(object.__dict__.keys())
#values = ', '.join([ str(col) for col in object.__dict__.values()])

#print(columns)
#print(values)

# Crear la ventana principal

root = tk.Tk()
root.title("Aplicación SQL")

connectStr='examenquiz/123@localhost:1521/xepdb1'


def save_object(objeto):
    # Conectarse a la base de datos Oracle
    connection = cx_Oracle.connect(connectStr)
    cursor = connection.cursor()
# Obtener los nombres de los parámetros automáticamente
    parametros = objeto.__dict__
    table_name=objeto.__class__.__name__
        # Preparar la consulta SQL
    sql = "INSERT INTO {} ({}) VALUES ({})".format(
        table_name,
        ', '.join(parametros.keys()),
        ', '.join(':' + str(i + 1) for i in range(len(parametros)))
    )

        # Ejecutar la consulta SQL
    cursor.execute(sql, list(parametros.values()))

    # Confirmar la transacción y cerrar la conexión
    connection.commit()
    cursor.close()
    connection.close()
    
   

'''
    # Crear los widgets de la interfaz
label_idcliente = tk.Label(root, text="ID Cliente:")
label_idcliente.pack()
entry_idcliente = tk.Entry(root)
entry_idcliente.pack()

label_nombre = tk.Label(root, text="Nombre:")
label_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

label_apellido = tk.Label(root, text="Apellido:")
label_apellido.pack()
entry_apellido = tk.Entry(root)
entry_apellido.pack()

label_email = tk.Label(root, text="Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

label_telefono = tk.Label(root, text="Teléfono:")
label_telefono.pack()
entry_telefono = tk.Entry(root)
entry_telefono.pack()


boton_insertar = tk.Button(root, text="Insertar datos", command=lambda: save_object(Clientes(int(entry_idcliente.get()),entry_nombre.get(),entry_apellido.get(),entry_email.get(),entry_telefono.get())))    
boton_insertar.pack()

# Iniciar el bucle principal de la aplicación
root.mainloop()


#juan = Clientes(22, "Juan", "Perez", "juan@email.com", "555-1234")

# Guardar la instancia en la base de datos
#save_object(juan,"Clientes")
'''
    