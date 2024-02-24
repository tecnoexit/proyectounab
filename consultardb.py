import mysql.connector

# Conectarse al servidor MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="GibraN@1980",
    database="sensor"
)

# Crear el cursor
cursor = connection.cursor()

# Consulta SQL para seleccionar todos los datos de la tabla
sql = "SELECT * FROM BROWN"

# Ejecutar la consulta
cursor.execute(sql)

# Obtener todos los resultados
results = cursor.fetchall()

# Mostrar los resultados
for row in results:
    print(row)

# Cerrar cursor y conexión
cursor.close()
connection.close()
