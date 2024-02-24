import os

# Instalar MySQL y sus dependencias
os.system('sudo apt-get update')
os.system('sudo apt-get install mysql-server mysql-client')

# Instalar el conector Python para MySQL
os.system('pip install mysql-connector-python')
