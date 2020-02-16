import grpc
from concurrent import futures
import time

# importo las clases generadas por el compilador de IDL
import calculadora_pb2
import calculadora_pb2_grpc

# importo el archivo original
import calculadora

# creo una clase para definir la funcionalidad del sistema
class ServicioCalculadora (calculadora_pb2_grpc.CalculadoraServicer):
    # exponemos calculadora.raizCuadrada
    # el requerimiento y la respuesta es del tipo de datos calculadora_pb2.Numero
    def raizCuadrada (self, request, context):
        respuesta = calculadora_pb2.Numero()
        respuesta.valor = calculadora.raizCuadrada(request.valor)
        return respuesta

# creo un servidor gRPC
servidor = grpc.server(futures.ThreadPoolExecutor(max_workers = 10))

# uso la func. generada en calculadora_pb2_grpc
# denominada add_CalculadoraServicer_to_server
# para agregar la clase definida al servidor
calculadora_pb2_grpc.add_CalculadoraServicer_to_server(ServicioCalculadora(), servidor)

print("Iniciando servidor en el puerto 5000...")
# escucho en el puerto 5000
servidor.add_insecure_port('[::]:5000')
# inicio el servidor
servidor.start()

# dado que servidor.start() no se bloquea
# se agrega un bucle con un sleep() para mantenerlo funcionando
try:
    while  True:
        time.sleep(60000)
except KeyboardInterrupt:
    servidor.stop(0)
