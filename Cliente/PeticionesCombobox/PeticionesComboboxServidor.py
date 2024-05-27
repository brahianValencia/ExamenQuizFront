import cx_Oracle


def opcionesComboBox(table_name,column):
    # Conectarse a la base de datos Oracle
    connectStr='examenquiz/123@localhost:1521/xepdb1'
    connection = cx_Oracle.connect(connectStr)
    cursor = connection.cursor()
    cursor.execute(f"SELECT {column} FROM {table_name}")
    values = cursor.fetchall()
    # Crear una lista con los valores de la columna
    ArrayValues = [row[0] for row in values]
    

    # Cerrar el cursor y la conexión
    cursor.close()
    connection.close()

    return ArrayValues

