
import sys
import time
import zmq

PUERTO = "5556"

if len(sys.argv) > 1:
    PUERTO =  sys.argv[1]

if len(sys.argv) > 2:
    print("Error en argumentos.")
    exit(1)

contexto = zmq.Context()
publicador = contexto.socket(zmq.PUB)
publicador.bind("tcp://*:%s" % PUERTO)
i = 0

while True:
    i = i + 1
    time.sleep(5)
    # Envio mensajes
    publicador.send_multipart(["Deportes", "Info sobre deportes..." + str(i)])
    publicador.send_multipart(["Distribuidos", "Info sobre sistemas distribuidos..." + str(i)])

# no llega pero es una forma de especificar que se debe
# cerrar el socket y el contexto
publicador.close()
contexto.term()
