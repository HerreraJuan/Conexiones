import grpc
from sys import *
import time

# importo las clases generadas por el compilador de IDL
import calculadora_pb2
import calculadora_pb2_grpc

if (len(argv) <> 2):
	print("Error en argumentos")
	exit(1)

# abro un canal rpc
canal = grpc.insecure_channel('localhost:5000')

# creo un stub del cliente y asocio al canal
stub = calculadora_pb2_grpc.CalculadoraStub(canal)

# creo un mensajes de requerimiento
numero = calculadora_pb2.Numero(valor = int(argv[1]))

# realizo la llamada
print("Llamando a RPC...")
respuesta = stub.raizCuadrada(numero)

# imprimo respuesta
print("Raiz cuadrada de " + argv[1] + " es: " + str(respuesta.valor))

# llamada asincronica
futura_respuesta = stub.raizCuadrada.future(numero)

# espero
for i in (range(0,5)):
	print("...")
	time.sleep(1)

# obtengo respuesta e imprimo
asinc_respuesta = futura_respuesta.result()
print("Raiz cuadrada de " + argv[1] + " es: " + str(asinc_respuesta.valor))
