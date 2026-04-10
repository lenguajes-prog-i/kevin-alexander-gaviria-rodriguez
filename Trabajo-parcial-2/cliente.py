import socket
import threading
import sys
import pickle

class ChatClient:
    def __init__(self, host='192.168.1.226', port=5555): 
        # Se crea el socket del cliente (TCP)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        try:
            # Se conecta al servidor
            self.client.connect((host, port))
        except:
            # Si falla la conexión
            print("Error: Servidor no disponible.")
            sys.exit()

        # Se pide el nombre del usuario
        self.nickname = input("Ingresa tu nombre: ")
        
        # Control del estado del cliente
        self.running = True

    def receive_messages(self):
        # Método que recibe mensajes del servidor
        while self.running:
            try:
                # Recibe datos serializados
                data = self.client.recv(1024)
                
                # Convierte los datos (pickle → texto)
                message = pickle.loads(data)
                
                # Si el servidor solicita nickname
                if message == "NICKNAME_REQUEST":
                    # Envía el nickname serializado
                    self.client.send(pickle.dumps(self.nickname))
                else:
                    # Muestra el mensaje recibido
                    print(f"\r{message}\n> ", end="")

            except:
                # Si se pierde la conexión
                if self.running:
                    print("\n[!] Conexión cerrada.")
                break

    def send_messages(self):
        # Lista de comandos disponibles
        print("Comandos: /join <sala>, /leave, /rooms, /msg <texto>, /pm <nick> <mensaje>, /quit")
        
        # Método para enviar mensajes
        while self.running:
            try:
                # Entrada del usuario
                msg = input("> ")
                
                # Envía el mensaje serializado
                self.client.send(pickle.dumps(msg))
                
                # Si el usuario decide salir
                if msg == "/quit":
                    self.running = False
                    break

            except:
                break
        
        # Cierra la conexión
        self.client.close()

    def start(self):
        # Hilo para recibir mensajes al mismo tiempo
        threading.Thread(target=self.receive_messages, daemon=True).start()
        
        # Ejecuta el envío de mensajes
        self.send_messages()

# Punto de entrada
if __name__ == "__main__":
    ChatClient().start()
