import zmq
import sys
import time

PUERTO = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:%s" % PUERTO)
i = 0
while True:
	i = i + 1
	socket.send("Servidor enviando mensaje a cliente..." + str(i))
	mensaje = socket.recv()
	print(mensaje + str(i))
	time.sleep(5)
