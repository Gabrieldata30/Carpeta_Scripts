# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 02:01:44 2024

@author: Usuario
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 01:50:04 2024

@author: Usuario
"""

import socket 

HOST="127.0.0.1"
PORT=8000

address=(HOST,PORT)

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket_cliente:
    socket_cliente.connect(address)
    print("Conectado con  EXITO")
    
    socket_cliente.send(b'Yo tu cliente te saludo')
    data=socket_cliente.recv(1024)
    
print('Recibido',repr(data))