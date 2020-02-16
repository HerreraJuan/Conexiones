import zmq
import sys

PUERTO1 = "5556"

if len(sys.argv) > 1:
	PUERTO1 =  sys.argv[1]

if len(sys.argv) > 2:
	PUERTO2 =  sys.argv[2]

contexto  = zmq.Context()
print ("Conectando a los servidores...")
socket = contexto.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % PUERTO1)
if len(sys.argv) > 2:
	socket.connect ("tcp://localhost:%s" % PUERTO2)

for i in range (1,10):
	print ("Enviando requerimiento ", i,"...")
	socket.send ("Hola")
	mensaje = socket.recv()
	print ("Respuesta recibida a requerimiento ", i, "[", mensaje, "]")