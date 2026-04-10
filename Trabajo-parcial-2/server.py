import socket
import threading

class ChatServer:
    def __init__(self, host='192.168.1.226', port=5555):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Permite reiniciar rápido el server
        self.server.bind((host, port))
        self.server.listen()
        
        self.clients = {}      # {socket: nickname}
        self.client_room = {}  # {socket: room_name}
        self.rooms = {}        # {room_name: [socket1, socket2]}
        
        print(f"=== SERVIDOR ===\n[INFO] Servidor iniciado en {host}:{port}")

    def broadcast(self, message, room, sender_socket=None):
        if room in self.rooms:
            for client in self.rooms[room]:
                if client != sender_socket:
                    try:
                        client.send(message.encode())
                    except:
                        self.remove_client(client)

    def remove_client(self, client):
        nickname = self.clients.get(client, "Usuario desconocido")
        if client in self.client_room:
            room = self.client_room[client]
            if client in self.rooms.get(room, []):
                self.rooms[room].remove(client)
            del self.client_room[client]

        if client in self.clients:
            del self.clients[client]
            
        client.close()
        print(f"[-] {nickname} desconectado")

    def handle_client(self, client):
        """Gestiona la comunicación. Ahora el Nickname se pide aquí."""
        try:
            # Protocolo inicial de Nickname
            client.send("NICKNAME_REQUEST".encode())
            nickname = client.recv(1024).decode().strip()
            if not nickname: nickname = f"User_{client.getpeername()[1]}"
            self.clients[client] = nickname
            print(f"[NUEVO] {nickname} se ha conectado.")

            while True:
                msg = client.recv(1024).decode().strip()
                if not msg: break

                # Lógica de Comandos
                if msg.startswith("/join"):
                    parts = msg.split()
                    if len(parts) < 2:
                        client.send("Error: Uso /join <sala>".encode())
                    elif client in self.client_room:
                        client.send("Error: Ya estás en una sala. Usa /leave.".encode())
                    else:
                        room = parts[1]
                        self.client_room[client] = room
                        self.rooms.setdefault(room, []).append(client)
                        client.send(f"[INFO] Te has unido a '{room}'".encode())
                        print(f"[+] {nickname} -> sala '{room}'")

                elif msg == "/leave":
                    if client in self.client_room:
                        room = self.client_room.pop(client)
                        self.rooms[room].remove(client)
                        client.send(f"[INFO] Saliste de '{room}'".encode())
                    else:
                        client.send("Error: No estás en ninguna sala.".encode())

                elif msg == "/rooms":
                    lista = ", ".join(self.rooms.keys()) if self.rooms else "Ninguna"
                    client.send(f"Salas: {lista}".encode())

                elif msg.startswith("/msg"):
                    if client not in self.client_room:
                        client.send("Error: Únete a una sala primero.".encode())
                    else:
                        parts = msg.split(" ", 1)
                        if len(parts) > 1:
                            room = self.client_room[client]
                            self.broadcast(f"{nickname}: {parts[1]}", room, client)

                elif msg == "/quit":
                    break
                else:
                    client.send("Comando no válido.".encode())
        except:
            pass
        finally:
            self.remove_client(client)

    def run(self):
        while True:
            client, addr = self.server.accept()
            # El hilo ahora se encarga de TODO el proceso del cliente
            thread = threading.Thread(target=self.handle_client, args=(client,), daemon=True)
            thread.start()

if __name__ == "__main__":
    ChatServer().run()