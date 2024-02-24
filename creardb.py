import mysql.connector

# Conectarse al servidor MySQL
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="GibraN@1980"
)

# Crear la base de datos
cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS sensor")
cursor.execute("USE sensor")

# Crear la tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS BROWN (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    temperatura FLOAT,
    sensacion_termica FLOAT,
    presion FLOAT
)
""")

# Cerrar cursor y conexión
cursor.close()
connection.close()
