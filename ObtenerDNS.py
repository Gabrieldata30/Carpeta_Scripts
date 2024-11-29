# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 01:35:36 2024

@author: Usuario
"""

import socket

ip_IN=input("Ingrese la ip que quieres  obtener su DNS: ")


try:
    dominio=socket.gethostbyaddr(ip_IN)[0]
    print("Se obtuvo el dominio")
    print("LA IP ES %s , y tiene el dominio %s" %(ip_IN,dominio)) #hallar el dominio DNS con una IP
    
    
except socket.error as msg:
    print("%s: %s" % (ip_IN,msg))