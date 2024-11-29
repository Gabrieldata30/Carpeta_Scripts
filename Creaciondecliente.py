
"Script_conectarservidor"
import socket


s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #CONEXION UDP socket.SOCK_DGRAM

print("Socket creado")

host_ip=socket.gethostbyname("www.google.com")

port=80

address=(host_ip,port)


s.connect(address)

print("Conexion OK")

print("IP Destino = ",host_ip)
print("Puerto destino= ",port)