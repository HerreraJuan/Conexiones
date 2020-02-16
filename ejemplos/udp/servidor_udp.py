import socket
import sys

# se crea un socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# se define la dir.
direccion = ('localhost', 7000)
# se asocia la dir. al socket
sock.bind(direccion)

while True:
    # se espera por un mensaje (4096 bytes de buffer)
    # devuelve datos y dir. de donde se ha enviado
    datos, dir_env = sock.recvfrom(4096)

    print ("Recibido de: " + str(dir_env))
    print ("Datos recepcionados: " + datos)

    if datos:
		# se envian datos recibidos (servidor de eco)
        enviar = sock.sendto(datos, dir_env)
        print ("Datos enviados..")
