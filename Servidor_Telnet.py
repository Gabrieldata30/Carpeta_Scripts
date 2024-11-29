# -*- coding: utf-8 -*-
"""
telnet
"""
 
import socket

socket_servidor=socket.socket()

port=12345

socket_servidor.bind(('',port))

print("El socket esta enlazado a ",port)

socket_servidor.listen(5)


while True:
    con,addr=socket_servidor.accept()
    print("Conexion recibida de : ",addr)
    con.send(b'Gracias por conectarse')
    
    con.close()