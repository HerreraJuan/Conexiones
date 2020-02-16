import zmq
import time
import sys

PUERTO = "5556"
if len(sys.argv) > 1:
	PUERTO =  sys.argv[1]

contecto = zmq.Context()
socket = contecto.socket(zmq.REP)
socket.bind("tcp://*:%s" % PUERTO)

while True:
	mensaje = socket.recv()                   # espera por el requerimiento de un cliente
	print "Requerimiento recibido: ", mensaje # imprime lo recibido
	time.sleep(5)
	socket.send("Respuesta de  %s" % PUERTO)  # mando respuesta
