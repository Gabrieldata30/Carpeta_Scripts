# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 01:50:04 2024

@author: Usuario
"""

import socket 

HOST=''
PORT=8000

address=(HOST,PORT)

with socket.socket() as socket_servidor:
    socket_servidor.bind(address)
    socket_servidor.listen()
    
    conn,addr=socket_servidor.accept()
    
    with conn:
        print(f"conexion con el cliente IP ({addr[0]}) puerto ({addr[1]})")
        while True:
            data=conn.recv(1024)
            print(data)
            
            if data==b'0':
                break
            conn.sendall(b'Mensaje recibido')
            