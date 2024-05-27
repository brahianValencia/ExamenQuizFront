import cx_Oracle
import os

def create_classes():
    # Conectarse a la base de datos Oracle
    connectStr='examenquiz/123@localhost:1521/xepdb1'
    connection = cx_Oracle.connect(connectStr)
    cursor = connection.cursor()
    # Obtener información de las tablas
    cursor.execute("SELECT table_name FROM user_tables")
    tables = cursor.fetchall()
    # Crear un directorio para las clases generadas
    os.makedirs("Servidor/Entidades", exist_ok=True)
    
    for table in tables:
        table_name = table[0]
        class_name = ''.join(word.capitalize() for word in table_name.split('_'))
        file_name = f"Servidor/Entidades/{class_name}.py"

        cursor.execute(f"SELECT column_name, data_type FROM user_tab_columns WHERE table_name = '{table_name}'")
        columns = cursor.fetchall()
        class_definitionAttributes=""

        with open(file_name, "w") as f:
            class_definition = f"class {class_name}:\n"
            #class_definition += "    def __init__(self):\n"
            class_definition += "    def __init__(self,"
            class_definitionAttributes=""
            

            for i,column in enumerate(columns):
                column_name = column[0]
                data_type = column[1]
                class_definitionAttributes += f"       self.{column_name} = {column[0]}  # {data_type}\n"
                if i!=len(columns)-1:
                    class_definition+=column_name+", "
                else:
                 class_definition+=column_name+"):\n"
                 class_definition+=class_definitionAttributes
        
            
            f.write(class_definition)  
                
                
    # Confirmar la transacción y cerrar la conexión
    connection.commit()
    cursor.close()
    connection.close()
    
    
create_classes()
