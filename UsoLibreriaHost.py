# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 00:16:39 2024

@author: Usuario
"""

import ipaddress


network_input=input("Ingrese un host/mask: ")

network=ipaddress.IPv4Network(network_input,strict=False)

print("Direccion de red= ",network.network_address)

print("Broadcast: ",network.broadcast_address)

print("Mascara de red: ",network.netmask)

print("Red y mascara de host: ",network.with_hostmask)

print("Longitud de la mascara de red: ",network.prefixlen)

print("Numero de hosts= ",network.num_addresses-2)