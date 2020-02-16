from socket import *
from sys import *
from datetime import datetime *
from datetime import date*

if (len(argv) > 2):
	print("Error en argumentos")
	exit(1)

HOST = '127.0.0.1'
PUERTO = int(argv[1])

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PUERTO))
s.listen(1)
while True:                       # bucle infinito
	(conn, addr) = s.accept() # retorna un nuevo socket y direccion del cliente
	datos = conn.recv(1024)   # recibe datos del cliente (1024 bytes)
	if not datos: break       # se detiene si el cliente se detiene
	conn.send(str(datos)+"*") # retorna al cliente el valor recibido + "*"
	conn.close()              # cierra la conexion con el cliente
