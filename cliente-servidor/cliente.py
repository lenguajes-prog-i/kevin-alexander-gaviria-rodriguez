import socket

HOST = "localhost"
PORT = 5002

# socket TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexion
client.connect((HOST, PORT))

# mensaje
mensaje = "Hola servidor"
client.send(mensaje.encode())

# repuesta
respuesta = client.recv(1024).decode()
print(f"Respuesta del servidor: {respuesta}")

client.close()