# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 00:02:01 2024

@author: Usuario
"""

import ipaddress

ip_INPUT=input("Ingrese IP host: ")

ip=ipaddress.IPv4Address(ip_INPUT) #cambiar address por Network y se agrega el ,strict = false para que sea por subred

print("Bits en la IP = ",ip.max_prefixlen)

print("Es multicast= ",ip.is_multicast)

print("Privada= ",ip.is_private)

print("Public= ",ip.is_global)

print("Reservada= ",ip.is_reserved)

print("LOOPBACK= ",ip.is_loopback)

ip1=ip+12

print("LA NUEVA IP : ",ip1)