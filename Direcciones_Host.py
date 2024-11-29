# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 01:13:25 2024

@author: Usuario
"""

import socket

direcciones=socket.getaddrinfo(socket.gethostname(),None) #obteber direcciones de tu host

print(type(direcciones))


for ip in direcciones:
     
    if(ip[0]==socket.AF_INET6): #SOLO PARA IMPRIMIR DIRECCIONES IPV6 SINO ELIMINA ESTE IF
       print(ip [4] [0])