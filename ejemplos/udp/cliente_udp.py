import socket
import sys

# Se crea un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

dir_serv = ('localhost', 7000)
msj = "Prueba UDP..."
try:
    # se envian datos
    env = sock.sendto(msj, dir_serv)

    # se recibe la respuesta (buffer de 4096 bytes)
    # devuelve datos y dir. de donde se ha enviado
    datos, dir_env = sock.recvfrom(4096)
    print ("Recibido de: " + str(dir_env))
    print ("Datos recepcionados: " + datos)
finally:
    print ("Finalizando, se cierra socket...")
    sock.close()
