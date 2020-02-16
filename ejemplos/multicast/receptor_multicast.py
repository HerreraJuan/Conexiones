#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import struct

dir_multicast = '225.0.0.37'
puerto = 12345

#defino socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# reuso dir.
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# asocio socket a un determinado puerto
sock.bind(('', puerto))
# agrego receptor al grupo multicast
m = struct.pack("4sl", socket.inet_aton(dir_multicast), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, m)

while 1:
	# espero por mensajes
	msj, direc = sock.recvfrom(255)
	print (str(direc) + ": " + msj)
