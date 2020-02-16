import math
import time

def raizCuadrada(x):
    y = math.sqrt(x)
    # simulo una llamada larga
    time.sleep(10)
    return y
