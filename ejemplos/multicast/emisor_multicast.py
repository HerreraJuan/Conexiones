#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct
import sys

# mensaje a enviar
msj = "Prueba de multicast..."

# datos de dir. y puerto de multicast
# dir. posibles: 224.0.0.0 a 239.255.255.255
dir_multicast = '225.0.0.37'
puerto = 12345

# creo socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# defino tiempo de vida (time to live)
# 0 <= tiempo_de_vida <= 255
# 0 máquina, 1 red local, 32 zona, 128 continente, 255 sin restricción
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
# se envia un mensaje
sock.sendto(msj, (dir_multicast, puerto))
# se cierra el socket
sock.close()
