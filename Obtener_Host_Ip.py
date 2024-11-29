# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 01:05:49 2024

@author: Usuario
"""

import socket

host=socket.gethostname()

ip=socket.gethostbyname(host)

print("Nombre= %s ,ip=%s" %(host,ip))

