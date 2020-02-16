from socket import *
from sys import *

if (len(argv) > 3):
	print("Error en argumentos")
	exit(1)

HOST = argv[1]
PUERTO = int(argv[2])

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PUERTO)) # conecta al servidor (bloqueandose hasta que es aceptado)
s.send("Hola Mundo")      # envia datos (Hola Mundo)
datos = s.recv(1024)      # recibe la respuesta (hasta 1024 bytes)
print(datos)              # imprime la respuesta
s.close()                 # cierra la conexion
