import zmq
import sys
import time

#PUERTO = "5556"

if len(sys.argv) == 3:
    PUERTO =  sys.argv[1]
else:
    print("Error en argumentos.")
    exit(1)

contexto = zmq.Context()
subscriptor = contexto.socket(zmq.SUB)
subscriptor.connect("tcp://localhost:%s" % PUERTO)
subscriptor.setsockopt(zmq.SUBSCRIBE, sys.argv[2])

while True:
    # Envio mensajes
    [direccion, contenido] = subscriptor.recv_multipart()
    print("Llego: " + direccion + ". Contenido: " + contenido)

# no llega pero es una forma de especificar que se debe
# cerrar el socket y el contexto
publicador.close()
contexto.term()
