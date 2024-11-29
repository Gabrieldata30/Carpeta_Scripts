# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 23:47:24 2024

@author: Usuario
"""

import socket

socket_cliente=socket.socket()

port=12345


socket_cliente.connect(('127.0.0.1',port))

print(socket_cliente.recv(1024))

socket_cliente.close()