import zmq
import sys
import time

PUERTO = "5556"
context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:%s" % PUERTO)

while True:
	msg = socket.recv()
	print (msg)
	socket.send("mensaje cliente 1 a servidor")
	# socket.send("mensaje cliente 2 a servidor")
	time.sleep(10)
